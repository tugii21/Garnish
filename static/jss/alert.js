// Get the alert element
var alert = document.getElementById('loginAlert');

//  click event listener to the alert element, code allows the user to interact with the alert element by clicking on
alert.addEventListener('click', function (event) {
    if (event.target.classList.contains('btn-close') || event.target.id === 'okButton') {
        alert.classList.remove('show');
    }
});