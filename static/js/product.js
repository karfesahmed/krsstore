document.addEventListener("DOMContentLoaded",()=>{
    btn_quantity();
    
})

function btn_quantity(){
    const decrease = document.querySelector("#decrease");
    const increase = document.querySelector("#increase");
    const inp_quantity = document.querySelector("#quantity")
    const span_quantity = document.querySelector("#quan")
    const current_price = document.querySelector("#product_price")
    const total = document.querySelector("#total")
    let counter = 1;
    decrease.addEventListener("click",()=>{
        if(counter>1){
            counter--;
            inp_quantity.value = counter
            span_quantity.innerHTML = counter
            total.innerHTML = `${parseFloat(current_price.innerHTML)*counter }`
            console.log(parseFloat(current_price.innerHTML)*counter);
            
            
        }
    })
    increase.addEventListener('click',()=>{
        counter++;
        inp_quantity.value = counter
        span_quantity.innerHTML = counter
        total.innerHTML = `${parseFloat(current_price.innerHTML)*counter }`
        console.log(parseFloat(current_price.innerHTML)*counter);
    })
    
}

