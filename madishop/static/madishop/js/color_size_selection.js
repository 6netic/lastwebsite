/* Change picture depending on color selected */
if(document.getElementById("color-select")) {
    let img = document.getElementById("img-gallery");
    let colSelect = document.getElementById("color-select");
    //let colorSelected = colSelect.options[colSelect.selectedIndex].value;
    let colorSelected = colSelect.options[colSelect.selectedIndex].text;
    let imgDict = document.getElementById("imgDict").value;
    let tmp1Dict = imgDict.replace(/['{}]/g, "").split(", ");
    const cpList = [];
    for (let i = 0; i < tmp1Dict.length; i++) {
        cpList[i] = tmp1Dict[i].split(": ");
    }
    for(let i = 0; i < cpList.length; i++) {
        if(colorSelected === cpList[i][0]) {
            img.src = cpList[i][1];
        }
    }
    document.getElementById("colorSlt").value = colorSelected;
    // when color selection is modified :
    colSelect.addEventListener('change', function() {
        let colorSelected = colSelect.options[colSelect.selectedIndex].text;
        for(let i = 0; i < cpList.length; i++) {
            if(colorSelected === cpList[i][0]) {
                img.src = cpList[i][1];
            }
        }
        document.getElementById("colorSlt").value = colorSelected;
    });
}

/* Change selected size */
if(document.getElementById("size-select")) {
    let sizeSelect = document.getElementById("size-select");
    let sizeSelected = sizeSelect.options[sizeSelect.selectedIndex].value;
    document.getElementById("sizeSlt").value = sizeSelected;
    // when size selection is changed :
    sizeSelect.addEventListener('change', function(){
        let sizeSelected = sizeSelect.options[sizeSelect.selectedIndex].value;
        document.getElementById("sizeSlt").value = sizeSelected;
    });
}
