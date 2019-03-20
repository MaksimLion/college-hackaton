var btnStart = document.getElementById('start');
var btnClose = document.getElementById('close');
btnStart.onclick = displayRegister;
btnClose.onclick = hiddenRegister;
var form = document.getElementsByClassName('register-form')[0];
var container = document.getElementsByClassName('container')[0];

function displayRegister(){
    container.style.opacity = "0.3";
    form.style.display = "block";
}

function hiddenRegister(){
    container.style.opacity = "1.0";
    form.style.display = "none";
}

function register() {
    event.preventDefault()
    document.location.href = "/sign_up"
}