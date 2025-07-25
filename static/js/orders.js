document.addEventListener("DOMContentLoaded",()=>{
    orders_list();
})

function orders_list(){
    const table = document.querySelector("#orders");
    fetch(`http://localhost:8000/orderpilot/orders-list`).then(res=>res.json())
    .then((data)=>{
        
        const csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const tabs = document.querySelectorAll(".filter-tab");
        tabs.forEach(tab => {
            tab.addEventListener("click",()=>{
                table.innerHTML =``;
                data.forEach((order)=>{
                    if(order.confirmed=="0"){

                            if(tab.id == "0" && order.delivery_type=="0"){
                                table.innerHTML += renderOrderRow(order,csrf_token);
                            }else if(tab.id == "1" && order.delivery_type=="1"){
                                table.innerHTML += renderOrderRow(order,csrf_token);
                            }else if(tab.id == "2" && order.delivery_type=="2"){
                                table.innerHTML += renderOrderRow(order,csrf_token);
                            }else if(tab.id == "3" && order.delivery_type=="3"){
                                table.innerHTML += renderOrderRow(order,csrf_token);
                            }else if(tab.id == "4" && order.delivery_type=="4"){
                                table.innerHTML += renderOrderRow(order,csrf_token);
                            }
                                        
                    }
                })
            })
        })
        document.getElementById("0").dispatchEvent(new Event("click"));

    })
}

function renderOrderRow(order, csrf_token) {
  return `
    <form method="post">
      <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
      <div class="d-flex align-items-center border rounded shadow-sm mb-2 px-2 py-2 card-order" style="min-width: 1400px; font-size: 0.8rem;">
        
        <div style="width: 40px;">#${order.id}</div>
        <input type="hidden" name="order_id" value="${order.id}">

        <div style="width: 120px;">${order.Name}</div>
        <div style="width: 130px;">${order.Phone}</div>
        <div style="width: 100px;">${order.wilaya}</div>
        <div style="width: 200px;">${truncateText(order.Address, 25)}</div>

        <div style="width: 110px;">
          <select style="width: 90px;" class="form-select form-select-sm" name="shipping_to">
            <option value="0" ${order.order_type === "0" ? "selected":""}>Home</option>
            <option value="1" ${order.order_type === "1" ? "selected":""}>Office</option>
          </select>
        </div>

        <!-- Note -->
        <div style="width: 200px;">
          <textarea style="width: 180px;" name="note" class="form-control form-control-sm" rows="1" placeholder="...">${order.note || ""}</textarea>
        </div>

        <!-- Status -->
        <div style="width: 170px;">
          <select style="width: 150px;" class="form-select form-select-sm" name="status">
            <option value="0" ${order.delivery_type === "0" ? "selected":""}>Not Reviewed</option>
            <option value="1"${order.delivery_type === "1" ? "selected":""}>Confirmed</option>
            <option value="2"${order.delivery_type === "2" ? "selected":""}>Postponed</option>
            <option value="3"${order.delivery_type === "3" ? "selected":""}>No Answer</option>
            <option value="4"${order.delivery_type === "4" ? "selected":""}>Cancelled</option>
          </select>
        </div>

        <!-- Product, Quantity, Price -->
        <div style="width: 150px;">${truncateText(order.product, 18)}</div>
        <div style="width: 80px;">
          <input type="number" style="width: 60px;" name="new_quantity" value="${order.quantity}">
        </div>
        <div style="width: 100px;">
          <input type="text" style="width: 60px;" name="new_price" value="${order.total}"> DA
        </div>

        <div style="width: 110px;">
          <input type="submit" style="width: 90px;" class="btn btn-sm btn-primary sub"  value="✔ Confirm">
        </div>

      </div>
    </form>
  `;
}




function truncateText(text, maxLength) {
    if (text.length > maxLength) {
        return text.slice(0, maxLength) + "..";
    }
    console.log(text);
    
    return text;
}