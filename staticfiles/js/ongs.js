document.addEventListener("DOMContentLoaded", function () {
    var phoneInput = document.getElementById("id_phone");
    phoneInput.addEventListener("input", function () {
        phoneInput.value = phoneInput.value.replace(/\D/g, "");
    });
});