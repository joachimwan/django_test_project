function updateProject(id) {
    let hiddenable_element_ids = [
        "div-project-name-",
        "form-update-project-",
        "undo-button-toggle-update-project-",
        "delete-button-project-"
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
        "delete-button-well-"
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

function updateLookahead(id) {
    let hiddenable_element_ids = [
        "div-lookahead-name-",
        "form-update-lookahead-",
        "undo-button-toggle-update-lookahead-",
        "delete-button-lookahead-"
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

function updatePhase(id) {
    let hiddenable_element_ids = [
        "div-phase-name-",
        "form-update-phase-",
        "undo-button-toggle-update-phase-",
        "delete-button-phase-"
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

function updateStep(id) {
    let hiddenable_element_ids = [
        "div-step-name-",
        "form-update-step-",
        "undo-button-toggle-update-step-",
        "delete-button-step-"
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