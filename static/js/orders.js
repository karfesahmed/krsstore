document.addEventListener("DOMContentLoaded", () => {
  orders_list();
  const watchedBtn = document.getElementById("1");
    const form = document.getElementById("zr-form");

    function updateFormVisibility() {
      if (watchedBtn.classList.contains("active")) {
        form.style.display = "block";
      } else {
        form.style.display = "none";
      }
    }

    updateFormVisibility();
  const tabs = document.querySelectorAll(".filter-tab");
    tabs.forEach(tab => {
      tab.addEventListener("click", () => {
        tabs.forEach(t => t.classList.remove("active"));
        tab.classList.add("active");
        updateFormVisibility();
      })
    });
  // ✅ delegation for dynamic buttons
  document.querySelector("#orders").addEventListener("click", (e) => {
    if (e.target.classList.contains("sub")) {
      const btn = e.target;
      const order_id = btn.id;

      const order_type = document.querySelector(`#order_type_${order_id}`).value;
      const delivery_type = document.querySelector(`#delivery_type_${order_id}`).value;
      const Size = document.querySelector(`#size_${order_id}`).value || null;
      const Color = document.querySelector(`#color_${order_id}`).value;
      const quantity = parseInt(document.querySelector(`#quantity_${order_id}`).value);
      const total = document.querySelector(`#total_${order_id}`).value;
      const note = document.querySelector(`#note_${order_id}`).value;

      // تحديد التاب الحالي لتحديثه بعد الحفظ
      const current_tab = document.querySelector(".filter-tab.active")?.id || "0";

      change_status(order_id, order_type, delivery_type, Size, Color, quantity, total, note, current_tab);
    }
  });
});



function orders_list() {
  const table = document.querySelector("#orders");

  return fetch(`http://localhost:8000/orderpilot/orders-list`)
    .then((res) => res.json())
    .then((data) => {
      const tabs = document.querySelectorAll(".filter-tab");

      tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
          table.innerHTML = ``;

          data.forEach((order) => {
            if (order.confirmed === "0" && tab.id === order.delivery_type) {
              table.innerHTML += renderOrderRow(order);

            }
          });
        });
      });

      document.getElementById("0").dispatchEvent(new Event("click"));
    });
}

function renderOrderRow(order) {
  return `
    <div class="d-flex align-items-center border rounded shadow-sm mb-2 px-2 py-2 card-order" style="min-width: 1400px; font-size: 0.8rem;">
      
      <div style="width: 40px;">#${order.id}</div>
      <input type="hidden" name="order_id" value="${order.id}">

      <div style="width: 120px;">${order.Name}</div>
      <div style="width: 130px;">${order.Phone}</div>
      <div style="width: 100px;">${order.wilaya}</div>
      <div style="width: 200px;">${truncateText(order.Address, 25)}</div>

      <div style="width: 110px;">
        <select style="width: 90px;" id="order_type_${order.id}" class="form-select form-select-sm" name="shipping_to">
          <option value="0" ${order.order_type === "0" ? "selected" : ""}>Home</option>
          <option value="1" ${order.order_type === "1" ? "selected" : ""}>Office</option>
        </select>
      </div>

      <div style="width: 200px;">
        <textarea style="width: 180px;" id="note_${order.id}" name="note" class="form-control form-control-sm" rows="1" placeholder="...">${order.note || ""}</textarea>
      </div>

      <div style="width: 170px;">
        <select style="width: 150px;" id="delivery_type_${order.id}" class="form-select form-select-sm" name="status">
          <option value="0" ${order.delivery_type === "0" ? "selected" : ""}>Not Reviewed</option>
          <option value="1" ${order.delivery_type === "1" ? "selected" : ""}>Confirmed</option>
          <option value="2" ${order.delivery_type === "2" ? "selected" : ""}>Postponed</option>
          <option value="3" ${order.delivery_type === "3" ? "selected" : ""}>No Answer</option>
          <option value="4" ${order.delivery_type === "4" ? "selected" : ""}>Cancelled</option>
        </select>
      </div>

      <div style="width: 150px;">${truncateText(order.product, 18)}</div>

      <div style="width: 80px;">
        <input type="text" style="width: 60px;" id="color_${order.id}" name="new_color" value="${order.Color}">
      </div>

      <div style="width: 80px;">
        <input type="text" style="width: 60px;" id="size_${order.id}" name="new_Size" value="${order.Size || ""}">
      </div>

      <div style="width: 80px;">
        <input type="number" style="width: 60px;" id="quantity_${order.id}" name="new_quantity" value="${order.quantity}">
      </div>

      <div style="width: 100px;">
        <input type="text" style="width: 60px;" id="total_${order.id}" name="new_price" value="${order.total}">
      </div>

      <div style="width: 110px;">
        <button type="submit" style="width: 90px;" class="btn btn-sm btn-primary sub" id="${order.id}">✔ Confirm</button>
      </div>
    </div>
  `;
}

function getCSRFToken() {
  let cookieValue = null;
  const name = 'csrftoken';
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function change_status(order_id, order_type, delivery_type, Size, Color, quantity, total, note, filter_now) {
  fetch(`http://localhost:8000/orderpilot/order-detail/${order_id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken(),
    },
    body: JSON.stringify({
      order_type: order_type,
      delivery_type: delivery_type,
      Size: Size,
      Color: Color,
      quantity: quantity,
      total: total,
      note: note,
    }),
  })
    .then(response => {
      if (response.ok) {
        alert('Order updated successfully!');
        orders_list().then(() => {
          document.getElementById(filter_now).dispatchEvent(new Event("click"));
        });
      } else {
        response.json().then(data => {
          console.error("Validation error:", data);
          alert('Update failed: ' + JSON.stringify(data));
        });
      }
    })
    .catch(error => {
      console.error('Fetch error:', error);
      alert('Connection to the server failed.');
    });
}

function truncateText(text, maxLength) {
  if (text.length > maxLength) {
    return text.slice(0, maxLength) + "..";
  }
  return text;
}
