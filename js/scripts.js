const navbar = document.getElementsByTagName('nav')[0];
window.addEventListener('scroll', function(){
    console.log(window.scrollY);
    if(window.scrollY >1){
        navbar.classList.replace('bg-transparent','nav-color');
    } else if(this.window.scrollY <= 0){
        navbar.classList.replace('nav-color','bg-transparent')
    }
});

// const modal = document.getElementById('reservasi-modal')[0];
// window.addEventListener('onclick', function(){
//     console.log(window.onclick);
//     if(window.onclick >1){
//         modal.classList.replace('reservasi-modal');
//     } else if(this.window.onclick <= 0){
//         modal.classList.replace('reservasi-modal')
//     }
// });
