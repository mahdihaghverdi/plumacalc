function clearInput() {
    document.getElementById('userinput').value = ''
}

function removeLast() {
    let str = document.getElementById('userinput').value;
    document.getElementById('userinput').value = str.substring(0, str.length - 1);
}
