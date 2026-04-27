// What we will learn:
// - how to access elements in the DOM using getElementById
// - how to add event listeners to elements

function klik(){
    // alert("ahoj")
    let skore = Number(document.getElementById("skore").textContent);
    skore += 1;
    document.getElementById("skore").textContent = skore;
}

function input_text(event){
    if (event.key === "Enter"){
        let text = document.getElementById("inp1").value;
        let answ = "Špatně";
        if (text === "Janek") {
            answ = "Správně!";
        }
        alert(answ);
        document.getElementById("inp1").value = "";
    }
}

document.getElementById("t1").addEventListener("click",klik)
document.getElementById("inp1").addEventListener("keydown",input_text)

