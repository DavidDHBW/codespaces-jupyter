
function toggleText() {
    text = "text 1";
    text2 = "text 2";
    alert("TEST");
    if (document.getElementById("demo").innerHTML == text){
        document.getElementById("demo").innerHTML = text2;
        document.getElementById("button").innerHTML = text1;
    }
    else {
        document.getElementById("demo").innerHTML = text;
        document.getElementById("button").innerHTML = text2;
    }
}