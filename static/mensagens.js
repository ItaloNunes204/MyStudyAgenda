setTimeout(()=>{
    document.querySelector('#mensagemR').style.display = 'none';
},4000)

function tira_mensagem(){
    const cadastrar = document.getElementById('mensagemR');
    cadastrar.style.display = 'none';
}

function tira_confirmação(){
    const cadastrar = document.getElementById('confirmacao_card');
    cadastrar.style.display = 'none';
}