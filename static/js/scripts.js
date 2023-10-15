// navbar
const navbar = document.getElementsByTagName('nav')[0];
window.addEventListener('scroll', function(){
    console.log(window.scrollY);
    if(window.scrollY >1){
        navbar.classList.replace('bg-transparent','nav-color');
    } else if(this.window.scrollY <= 0){
        navbar.classList.replace('nav-color','bg-transparent')
    }
});

// btn-reservasi-modal
const modal= document.querySelector('#reservasi-modal');
const openModal= document.querySelector('.open-button');
const closeModal= document.querySelector('.close-button');

openModal.addEventListener('click',() => {
    modal.showModal();
});
closeModal.addEventListener('click',() => {
    modal.close();
});

