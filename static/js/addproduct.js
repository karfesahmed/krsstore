document.addEventListener("DOMContentLoaded",()=>{
    
    const image_box = document.querySelector("#image-box")
    const input = document.querySelector("#images")
    input.addEventListener("change",()=>{
        image_box.innerHTML = ``
        Array.from(input.files).map((img)=>{
            image_box.innerHTML +=  `<img src="${URL.createObjectURL(img)}" alt="error" class="selected_images">`
        })

    })


    const addSizeBtn = document.getElementById("add-size-btn");
    const sizesContainer = document.getElementById("sizes-container");

    addSizeBtn.addEventListener("click", () => {
      const sizeRow = document.createElement("div");
      sizeRow.classList.add("row", "align-items-center", "mb-2");

      sizeRow.innerHTML = `
        <div class="col-md-6">
          <input type="text" name="size[]" class="form-control" placeholder="Size" required>
        </div>
        <div class="col-md-5">
          <input type="number" name="size_price[]" class="form-control" placeholder="default price is product price" step="1" >
        </div>
        <div class="col-md-1 text-end">
          <button type="button" class="btn btn-danger remove-size-btn">x</button>
        </div>
      `;

      sizeRow.querySelector(".remove-size-btn").addEventListener("click", () => {
        sizeRow.remove();
      });

      sizesContainer.appendChild(sizeRow);
    });

    const addColorBtn = document.getElementById("add-color-btn");
    const colorsContainer = document.getElementById("colors-container");

    addColorBtn.addEventListener("click", () => {
      const colorId = Date.now(); // Unique ID for inputs
      const colorRow = document.createElement("div");
      colorRow.classList.add("row", "align-items-center", "mb-3");

      colorRow.innerHTML = `
        <div class="col-md-6">
          <input type="text" name="color[]" class="form-control" placeholder="Color name" required>
        </div>
        <div class="col-md-5">
          <input type="file" name="color_image[]" accept="image/*" class="form-control color-image-input" data-preview-id="preview-${colorId}" required>
          
        </div>
        <div class="col-md-1 text-end">
          <button type="button" class="btn btn-danger remove-color-btn">X</button>
        </div>
        <div id="preview-${colorId}" class="col-md-6 offset-md-6"></div>
      `;

      colorRow.querySelector(".remove-color-btn").addEventListener("click", () => {
        colorRow.remove();
      });

      // Add preview event
      const inputImage = colorRow.querySelector(".color-image-input");
      inputImage.addEventListener("change", (e) => {
        const previewBox = document.getElementById(e.target.dataset.previewId);
        const file = e.target.files[0];
        if (file) {
          previewBox.innerHTML = `<img src="${URL.createObjectURL(file)}" alt="preview" class="selected_images">`;
        } else {
          previewBox.innerHTML = "";
        }
      });

      colorsContainer.appendChild(colorRow);
    });
})