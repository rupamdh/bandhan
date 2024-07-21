const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')
const register = document.getElementById('register')
const closeBtn = document.getElementById('close-btn')

register.addEventListener('click', () => {
    myModal.style.display = 'block'
})

closeBtn.addEventListener('click', () => {
    myModal.style.display = 'none'
})