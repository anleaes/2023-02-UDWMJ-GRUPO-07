document.addEventListener("DOMContentLoaded", function () {
    var timeInput = document.getElementById("id_time");

    timeInput.addEventListener("input", function () {
        timeInput.value = timeInput.value.replace(/[^\d:]/g, "");
        timeInput.value = timeInput.value.replace(/:+/g, ":");

        var timeArray = timeInput.value.split(":");
        

        if (timeArray[0]) {
            var hours = parseInt(timeArray[0], 10);
            if (hours > 23) {
                timeArray[0] = "23";
            }
        }

        if (timeArray[1]) {
            var minutes = parseInt(timeArray[1], 10);
            if (minutes > 59) {
                timeArray[1] = "59";
            }
        }


        if (timeArray[0] && timeArray[0].length > 2) {
            timeArray[0] = timeArray[0].slice(0, 2);
        }
        if (timeArray[1] && timeArray[1].length > 2) {
            timeArray[1] = timeArray[1].slice(0, 2);
        }

        timeInput.value = timeArray.join(":");
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

        var currentYear = new Date().getFullYear();

        if (dateArray[2]) {
            var year = parseInt(dateArray[2], 10);
            if (year > currentYear) {
                dateArray[2] = Math.min(currentYear).toString();
            }
        }

        // Limitar o número de caracteres para o dia, mês e ano
        if (dateArray[0] && dateArray[0].length > 2) {
            dateArray[0] = dateArray[0].slice(0, 2);
        }
        if (dateArray[1] && dateArray[1].length > 2) {
            dateArray[1] = dateArray[1].slice(0, 2);
        }
        if (dateArray[2] && dateArray[2].length > 4) {
            dateArray[2] = dateArray[2].slice(0, 4);
        }

        dateInput.value = dateArray.join("/");
    });
});
