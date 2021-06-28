const nav=document.getElementById('nav-menu')
const toggleMenu=document.getElementById('nav-toggle') 
const closeMenu=document.getElementById('nav-close')
const navLink =document.querySelectorAll('.nav_link')
toggleMenu.addEventListener('click',()=>{
    nav.classList.toggle('show')
})
function linkaction(){
    nav.classList.remove('show')
}

closeMenu.addEventListener('click',linkaction)
navLink.forEach(n =>n.addEventListener('click', linkaction))