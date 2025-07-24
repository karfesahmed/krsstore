document.addEventListener("DOMContentLoaded",()=>{
    btn_quantity();
    const krsCards = document.querySelectorAll('.krs-card-option');
    krsCards.forEach(card => {
        card.addEventListener('click', () => {
        krsCards.forEach(c => c.classList.remove('krs-selected'));
        card.classList.add('krs-selected');
        card.querySelector('input[type="radio"]').checked = true;
        });
    });
})

function btn_quantity(){
    const decrease = document.querySelector("#decrease");
    const increase = document.querySelector("#increase");
    const inp_quantity = document.querySelector("#quantity")
    const span_quantity = document.querySelector("#quan")
    const current_price = document.querySelector("#product_price")
    const total = document.querySelector("#total")
    const wilaya = document.querySelector("#wilaya")
    const shipping = document.querySelector("#shipping")
    shipping.innerHTML = `select wilaya`
    let counter = 1;
    wilaya.addEventListener("change",()=>{
        total.innerHTML = `${parseFloat(current_price.innerHTML) + parseFloat(wilaya.value.split(",")[1]) }`
        counter = 1
        inp_quantity.value = counter
        span_quantity.innerHTML = counter
        shipping.innerHTML =`${wilaya.value.split(",")[1]} DZD`
    })


    


    decrease.addEventListener("click",()=>{

        if(counter>1){
            if(wilaya.value === ""){
                alert("please select your wilaya")
            }else{
                counter--;
                inp_quantity.value = counter
                span_quantity.innerHTML = counter
                total.innerHTML = `${parseFloat(current_price.innerHTML)*counter + parseFloat(wilaya.value.split(",")[1]) }`
                console.log(parseFloat(current_price.innerHTML)*counter + parseFloat(wilaya.value.split(",")[1]));
            }
        }
    })
    increase.addEventListener('click',()=>{
        if(wilaya.value === ""){
            alert("please select your wilaya")
        }else{
            counter++;
            inp_quantity.value = counter
            span_quantity.innerHTML = counter
            total.innerHTML = `${parseFloat(current_price.innerHTML)*counter + parseFloat(wilaya.value.split(",")[1])}`
            console.log(parseFloat(current_price.innerHTML)*counter + parseFloat(wilaya.value.split(",")[1]));
        }
    })
}



