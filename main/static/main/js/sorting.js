function testfunc () {
    let collection = document.getElementById("sortablelist").children;

    document.getElementById("demo").innerHTML = "";

    [...collection].forEach(function(item, index){
        document.getElementById("demo").innerHTML += index +1  + item.innerHTML;
    });
}
