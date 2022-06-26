var count = 0;
function increment() {
    count = count + 1;
    //console.log(count)
    document.getElementById("count-el").innerText = count;
}

function reset() {
    count = 0;
    document.getElementById("count-el").innerText = 0;
    document.getElementById("save-btn-text").innerText = "Previous Entries: "
}

function save() {
    console.log(document.getElementById("save-btn-text").textContent += count + " - ");
}