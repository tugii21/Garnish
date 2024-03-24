// Get the alert element
var alertElement = document.getElementById("loginAlert");

// Click event listener to the alert element
// code allows the user to interact with the alert element by clicking on
alertElement.addEventListener("click", function (event) {
    if (event.target.classList.contains("btn-close") || event.target.id === "okButton") {
        alertElement.classList.remove("show");
    }
});
