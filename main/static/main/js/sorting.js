function testfunc() {
    let collection = document.getElementById("sortablelist").children;

    document.getElementById("demo").innerHTML = "";

    [...collection].forEach(function(item, index){
        document.getElementById("demo").innerHTML += index +1  + item.innerHTML;
    });
}

function updateStepOrder(id) {
    let form = document.getElementById("form-update-step-order-"+id);
    let collection = document.getElementById("sortable-steps-list-"+id).children;

    [...collection].forEach(function(element, index){
        let stepId = parseInt(element.id.split("div-step-")[1]);
        document.getElementById("order-step-"+stepId).value = index+1;
    });
    form.submit();
}

function updatePhaseOrder(id) {
    let form = document.getElementById("form-update-phase-order-"+id);
    let collection = document.getElementById("sortable-phase-list-"+id).children;

    [...collection].forEach(function(element, index){
        let phaseId = parseInt(element.id.split("div-phase-")[1]);
        console.log(phaseId)
        document.getElementById("order-phase-"+phaseId).value = index+1;
    });
    form.submit();
}