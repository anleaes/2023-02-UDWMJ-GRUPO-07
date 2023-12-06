document.addEventListener("DOMContentLoaded", function () {
    var years_oldInput = document.getElementById("id_years_old");

    years_oldInput.addEventListener("input", function () {
        years_oldInput.value = years_oldInput.value.replace(/\D/g, "");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var weightInput = document.getElementById("id_weight");

    weightInput.addEventListener("input", function () {
        weightInput.value = weightInput.value.replace(/\D/g, "");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var heightInput = document.getElementById("id_height");

    heightInput.addEventListener("input", function () {
        heightInput.value = heightInput.value.replace(/\D/g, "");
    });
});