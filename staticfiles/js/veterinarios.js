document.addEventListener("DOMContentLoaded", function () {
    var crmInput = document.getElementById("id_crm");

    crmInput.addEventListener("input", function () {
        crmInput.value = crmInput.value.replace(/\D/g, "");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    var register_dateInput = document.getElementById("id_register_date");

    register_dateInput.addEventListener("input", function () {

        register_dateInput.value = register_dateInput.value.replace(/[^\d/]/g, "");

        
        register_dateInput.value = register_dateInput.value.replace(/\/+/g, "/");

        var register_dateArray = register_dateInput.value.split("/");

        if (register_dateArray[0]) {
            var day = parseInt(register_dateArray[0], 10);
           
            if (day > 31) {
                register_dateArray[0] = "31";
            }
        }

        if (register_dateArray[1]) {
            var month = parseInt(register_dateArray[1], 10);
            
            if (month > 12) {
                register_dateArray[1] = "12";
            }
        }

        if (register_dateArray[2]) {
            
            register_dateArray[2] = register_dateArray[2].slice(0, 4);
    
            var currentYear = new Date().getFullYear();
            if (parseInt(register_dateArray[2]) > currentYear) {
                register_dateArray[2] = currentYear.toString();
            }
        }

        register_dateInput.value = register_dateArray.join("/");
    });
});
