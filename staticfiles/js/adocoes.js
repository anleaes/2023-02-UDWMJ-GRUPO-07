document.addEventListener("DOMContentLoaded", function () {
    var hourInput = document.getElementById("id_hour");

    hourInput.addEventListener("input", function () {
        
        hourInput.value = hourInput.value.replace(/[^\d:]/g, "");

        hourInput.value = hourInput.value.replace(/:+/g, ":");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var dateInput = document.getElementById("id_date"); 

    dateInput.addEventListener("input", function () {

        dateInput.value = dateInput.value.replace(/[^\d/]/g, "");

        dateInput.value = dateInput.value.replace(/\/+/g, "/");

        var dateArray = dateInput.value.split("/");
        
        if (dateArray[0]) {
            var day = parseInt(dateArray[0], 10);
            if (day > 31) {
                dateArray[0] = "31";
            }
        }

        if (dateArray[1]) {
            var month = parseInt(dateArray[1], 10);
            if (month > 12) {
                dateArray[1] = "12";
            }
        }

        if (dateArray[2] && dateArray[2].length > 4) {
            dateArray[2] = dateArray[2].slice(0, 4);
        }

        dateInput.value = dateArray.join("/");
    });
});