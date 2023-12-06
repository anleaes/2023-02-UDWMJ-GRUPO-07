document.addEventListener('DOMContentLoaded', function () {
    var yearsOldValueInput = document.getElementById('id_years_old_value');

    yearsOldValueInput.addEventListener('input', function () {
        var inputValue = parseInt(yearsOldValueInput.value, 10);

        if (isNaN(inputValue) || inputValue < 0) {
            yearsOldValueInput.value = '';  
        } else if (inputValue > 25) {
            yearsOldValueInput.value = '25';  
        }
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