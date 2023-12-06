document.addEventListener("DOMContentLoaded", function () {
    var cpfInput = document.getElementById("id_cpf");

cpfInput.addEventListener("input", function () {
    cpfInput.value = cpfInput.value.replace(/\D/g, "");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var phoneInput = document.getElementById("id_phone");

phoneInput.addEventListener("input", function () {
    phoneInput.value = phoneInput.value.replace(/\D/g, "");
    });
});