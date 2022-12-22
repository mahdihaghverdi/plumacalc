function clearInput() {
    document.getElementById('userinput').value = ''
}

function removeLast() {
    let str = document.getElementById('userinput').value;
    document.getElementById('userinput').value = str.substring(0, str.length - 1);
}


function display(value) {
    let input = document.getElementById('userinput').value;
    document.getElementById('userinput').value = input + value;
}

function copyText(all, errors) {
    if (all) {
        if (errors) {
            const input = document.getElementById('input').innerText
            const errors = document.getElementById('errors').innerText
            navigator.clipboard.writeText(input + errors)
        } else {
            const input = document.getElementById('input').innerText
            const answer = document.getElementById('answer').innerText
            navigator.clipboard.writeText(input + '=' + answer)
        }
        const btnText = document.getElementById('copy-all')
        btnText.innerText = "Copied!"
        return
    }
    const input = document.getElementById('input').innerText
    navigator.clipboard.writeText(input)
    const btn = document.getElementById('copy-input')
    btn.innerText = 'Copied!'

}


function copyAnswer() {
    const answer = document.getElementById('anstocopy').innerText
    navigator.clipboard.writeText(answer)
    const temp = '<i class="bi bi-clipboard-check"></i>';
    document.getElementById('ansclip').classList.remove('bi-clipboard')
    document.getElementById('ansclip').classList.add('bi-clipboard-check-fill')
}

function copyPostfix() {
    const answer = document.getElementById('posttocopy').innerText
    navigator.clipboard.writeText(answer)
    const temp = '<i class="bi bi-clipboard-check"></i>';
    document.getElementById('postclip').classList.remove('bi-clipboard')
    document.getElementById('postclip').classList.add('bi-clipboard-check-fill')
}

function copyError() {
    const answer = document.getElementById('errortocopy').innerText
    navigator.clipboard.writeText(answer)
    const temp = '<i class="bi bi-clipboard-check"></i>';
    document.getElementById('errorclip').classList.remove('bi-clipboard')
    document.getElementById('errorclip').classList.add('bi-clipboard-check-fill')
}
