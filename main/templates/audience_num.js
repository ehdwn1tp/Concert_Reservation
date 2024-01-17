var plus = document.querySelector("#plus-btn")
var minus = document.querySelector("#minus-btn")
var result = document.querySelector("#num-result")

let i = 1;
plus.addEventListener("click", () => {
    i++
    result.textContent = i
})

minus.addEventListener("click", () => {
    if (i > 1){
        i--
        result.textContent = i
    }
})