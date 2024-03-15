// Get the alert element
var alert = document.getElementById('loginAlert');

// Add click event listener to the alert element
alert.addEventListener('click', function (event) {
    if (event.target.classList.contains('btn-close') || event.target.id === 'okButton') {
        alert.classList.remove('show');
    }
});