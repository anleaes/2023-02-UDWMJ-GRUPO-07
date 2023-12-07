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


var weight_valueInput = document.getElementById('id_weight_value');


weight_valueInput.addEventListener('input', function() {

    var inputValue = weight_valueInput.value;


    if (inputValue.length > 2) {
        weight_valueInput.value = inputValue.slice(0, 2);
    }
});

var height_valueInput = document.getElementById('id_height_value');


height_valueInput.addEventListener('input', function() {

    var inputValue = height_valueInput.value;


    if (inputValue.length > 2) {
        height_valueInput.value = inputValue.slice(0, 2);
    }
});