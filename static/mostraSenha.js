function mostraSenha(){
    var input = document.getElementById('senha')
    var btn = document.getElementById('btn-senha')

    if(input.type === 'password'){
        input.setAttribute('type','text')
        btn.classList.replace('fa-eye','fa-eye-slash')
    }else{
        input.setAttribute('type','password')
        btn.classList.replace('fa-eye-slash','fa-eye')
    }
}

function mostraConfSenha(){
    var input = document.getElementById('confsenha')
    var btn = document.getElementById('btn-confsenha')

    if(input.type === 'password'){
        input.setAttribute('type','text')
        btn.classList.replace('fa-eye','fa-eye-slash')
    }else{
        input.setAttribute('type','password')
        btn.classList.replace('fa-eye-slash','fa-eye')
    }
}
