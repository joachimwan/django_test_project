function updateProject(id) {
    var default_block = document.getElementById("project-"+id);
    if (default_block.style.display === "none") {
        default_block.style.display = "block";
    } else {
        default_block.style.display = "none";
    }

    var update_block = document.getElementById("update-project-"+id);
    if (update_block.style.display === "none") {
        update_block.style.display = "block";
    } else {
        update_block.style.display = "none";
    }

    var edit_button = document.getElementById("toggle-update-project-"+id);
    let hidden = edit_button.getAttribute("hidden");
    if (hidden) {
       edit_button.removeAttribute("hidden");
    } else {
       edit_button.setAttribute("hidden", "hidden");
    }
}

function updateWell(id) {
    var default_block = document.getElementById("well-"+id);
    if (default_block.style.display === "none") {
        default_block.style.display = "block";
    } else {
        default_block.style.display = "none";
    }

    var update_block = document.getElementById("update-well-"+id);
    if (update_block.style.display === "none") {
        update_block.style.display = "block";
    } else {
        update_block.style.display = "none";
    }

    var edit_button = document.getElementById("toggle-update-well-"+id);
    let hidden = edit_button.getAttribute("hidden");
    if (hidden) {
       edit_button.removeAttribute("hidden");
    } else {
       edit_button.setAttribute("hidden", "hidden");
    }
}