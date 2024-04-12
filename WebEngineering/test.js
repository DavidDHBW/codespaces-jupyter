
function toggleText() {
    text = "text 1";
    text2 = "text 2";
    alert("TEST");
    if (document.getElementById("demo").innerHTML == text){
        document.getElementById("demo").innerHTML = text2;
    }
    else document.getElementById("demo").innerHTML = text;
}