function updateProject(id) {
    let hiddenable_element_ids = [
        "div-project-name-",
        "form-update-project-",
        "undo-button-toggle-update-project-",
//        "button-delete-project-"
    ];
    hiddenable_element_ids.forEach(function(element_name){
        let element = document.getElementById(element_name+id);
        let hidden_attr = element.getAttribute("hidden");
        if (hidden_attr) {
            element.removeAttribute("hidden");
        } else {
            element.setAttribute("hidden", true);
        }
    });

    let other_buttons = document.querySelectorAll('[id^="button"]');
    other_buttons.forEach(function(element){
        let hidden_attr = element.getAttribute("hidden");
        if (hidden_attr) {
            element.removeAttribute("hidden");
        } else {
            element.setAttribute("hidden", true);
        }
    });
}

function updateWell(id) {
    let hiddenable_element_ids = [
        "div-well-name-",
        "form-update-well-",
        "undo-button-toggle-update-well-",
//        "button-delete-well-"
    ];
    hiddenable_element_ids.forEach(function(element_name){
        let element = document.getElementById(element_name+id);
        let hidden_attr = element.getAttribute("hidden");
        if (hidden_attr) {
            element.removeAttribute("hidden");
        } else {
            element.setAttribute("hidden", true);
        }
    });

    let other_buttons = document.querySelectorAll('[id^="button"]');
    other_buttons.forEach(function(element){
        let hidden_attr = element.getAttribute("hidden");
        if (hidden_attr) {
            element.removeAttribute("hidden");
        } else {
            element.setAttribute("hidden", true);
        }
    });
}