function updateProject(id) {
//    var element = document.getElementById("project-"+id);
//    if (elem.style.display === "none") {
//        default_block.style.display = "block";
//    } else {
//        default_block.style.display = "none";
//    }

    var element = document.getElementById("div-project-name-"+id);
    let hidden1 = element.getAttribute("hidden");
    if (hidden1) {
       element.removeAttribute("hidden");
    } else {
       element.setAttribute("hidden", true);
    }

    var b = document.getElementById("form-update-project-"+id);
    let hidden2 = b.getAttribute("hidden");
    if (hidden2) {
       b.removeAttribute("hidden");
    } else {
       b.setAttribute("hidden", true);
    }

    var c = document.getElementById("button-toggle-update-project-"+id);
    let hidden3 = c.getAttribute("hidden");
    if (hidden3) {
       c.removeAttribute("hidden");
    } else {
       c.setAttribute("hidden", true);
    }

    var d = document.getElementById("button-delete-project-"+id);
    let hidden4 = d.getAttribute("hidden");
    if (hidden4) {
       d.removeAttribute("hidden");
    } else {
       d.setAttribute("hidden", true);
    }
}

function updateWell(id) {
//    var default_block = document.getElementById("well-"+id);
//    if (default_block.style.display === "none") {
//        default_block.style.display = "block";
//    } else {
//        default_block.style.display = "none";
//    }

    var element = document.getElementById("div-well-name-"+id);
    let hidden1 = element.getAttribute("hidden");
    if (hidden1) {
       element.removeAttribute("hidden");
    } else {
       element.setAttribute("hidden", true);
    }

    var b = document.getElementById("form-update-well-"+id);
    let hidden2 = b.getAttribute("hidden");
    if (hidden2) {
       b.removeAttribute("hidden");
    } else {
       b.setAttribute("hidden", true);
    }

    var c = document.getElementById("button-toggle-update-well-"+id);
    let hidden3 = c.getAttribute("hidden");
    if (hidden3) {
       c.removeAttribute("hidden");
    } else {
       c.setAttribute("hidden", true);
    }

    var d = document.getElementById("button-delete-well-"+id);
    let hidden4 = d.getAttribute("hidden");
    if (hidden4) {
       d.removeAttribute("hidden");
    } else {
       d.setAttribute("hidden", true);
    }
}