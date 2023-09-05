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
function validaNome(){
    const input = document.getElementById('nome')
    const label = document.getElementById('labelNome')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Nome'
        input.setAttribute('style','border-color: blue')
    } else if (input.value.length < 5) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Nome *Insirir no minimo 5 caracteres'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Nome'
        input.setAttribute('style','border-color: green')
    }
}
function validaEmail(){
    const input = document.getElementById('email')
    const label = document.getElementById('labelEmail')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Email'
        input.setAttribute('style','border-color: blue')
    } else if (input.value.length < 5) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Email *Insirir no minimo 5 caracteres'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Email'
        input.setAttribute('style','border-color: green')
    }
}
function validaSenha(){
    const input = document.getElementById('senha')
    const label = document.getElementById('labelSenha')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Senha'
        input.setAttribute('style','border-color: blue')
    } else if (input.value.length < 8) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Senha *Insirir no minimo 8 caracteres'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Senha'
        input.setAttribute('style','border-color: green')
    }
}
function validaConfSenha(){
    const senha = document.getElementById('senha')
    const confsenha = document.getElementById('confsenha')
    const label = document.getElementById('labelConfSenha')
    const labelSenha = document.getElementById('labelSenha')

    if(confsenha.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Confirmar senha'
        confsenha.setAttribute('style','border-color: blue')
        validaSenha()
    }else if(confsenha.value != senha.value){
        label.setAttribute('style','color: red')
        label.innerHTML = 'Confirmar Senha *As senhas não conferem '
        confsenha.setAttribute('style','border-color: red')

        labelSenha.setAttribute('style','color: red')
        labelSenha.innerHTML = 'Senha *As senhas não conferem '
        senha.setAttribute('style','border-color: red')
    }else{
        label.setAttribute('style','color: green')
        label.innerHTML = 'Confirmar Senha'
        confsenha.setAttribute('style','border-color: green')

        labelSenha.setAttribute('style','color: green')
        labelSenha.innerHTML = 'Senha'
        senha.setAttribute('style','border-color: green')
    }
}
function validaCurso(){
    const input = document.getElementById('curso')
    const label = document.getElementById('labelCurso')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Curso'
        input.setAttribute('style','border-color: blue')
    } else if (input.value.length < 3) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Curso *Insirir no minimo 3 caracteres'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Curso'
        input.setAttribute('style','border-color: green')
    }
}
function validaPeriodo(){
    const input = document.getElementById('periodo')
    const label = document.getElementById('labelPeriodo')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Periodo'
        input.setAttribute('style','border-color: blue')
    } else if (input.value < 0) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Periodo *Insirir um numero positivos'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Periodo'
        input.setAttribute('style','border-color: green')
    }
}
function validaUniversidade(){
    const input = document.getElementById('universidade')
    const label = document.getElementById('labelUniversidade')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Universidade'
        input.setAttribute('style','border-color: blue')
    } else if (input.value.length < 3) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Universidade *Insirir no minimo 3 caracteres'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Universidade'
        input.setAttribute('style','border-color: green')
    }   
}
function validaInicio(){
    const input = document.getElementById('inicio')
    const label = document.getElementById('labelInicio')
    if(input.value.length != 0){
        label.setAttribute('style','color: green')
        input.setAttribute('style','border-color: green')
    }else{
        label.setAttribute('style','color: blue')
        input.setAttribute('style','border-color: blue')
    }
}
function validaHorario(){
    const input = document.getElementById('horario')
    const label = document.getElementById('labelHorario')
    if(input.value.length != 0){
        label.setAttribute('style','color: green')
        input.setAttribute('style','border-color: green')
    }else{
        label.setAttribute('style','color: blue')
        input.setAttribute('style','border-color: blue')
    }
}
function validaLugar(){
    const input = document.getElementById('lugar')
    const label = document.getElementById('labelLugar')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Lugar'
        input.setAttribute('style','border-color: blue')
    } else if (input.value.length < 3) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Lugar *Insirir no minimo 3 caracteres'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Lugar'
        input.setAttribute('style','border-color: green')
    }
}
function validaObservacao(){
    const input = document.getElementById('observacao')
    const label = document.getElementById('labelObservacao')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Observação'
        input.setAttribute('style','border-color: blue')
    } else if (input.value.length < 3) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Observação *Insirir no minimo 3 caracteres'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Observação'
        input.setAttribute('style','border-color: green')
    }
}
function validaTipo(){
    const input = document.getElementById('tipo')
    const label = document.getElementById('labelTipo')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Tipo'
        input.setAttribute('style','border-color: blue')
    } else if (input.value.length < 3) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Tipo *Insirir no minimo 3 caracteres'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Tipo'
        input.setAttribute('style','border-color: green')
    }
}
function validaCreditos(){
    const input = document.getElementById('creditos')
    const label = document.getElementById('labelCreditos')
    if(input.value.lengt === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'N° Creditos'
        input.setAttribute('style','border-color: blue')
    } else if (input.value < 0 || input.value == 0 ) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'N° Creditos *Insirir um numero positivos'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'N° Creditos'
        input.setAttribute('style','border-color: green')
    }
}
function validaNota(){
    const input = document.getElementById('nota')
    const label = document.getElementById('labelNota')
    if(input.value.length === 0){
        label.setAttribute('style','color: blue')
        label.innerHTML = 'Nota da Atividade'
        input.setAttribute('style','border-color: blue')
    } else if (input.value < 0 || input.value == 0) {
        label.setAttribute('style','color: red')
        label.innerHTML = 'Nota da Atividade *Insirir um numero positivo'
        input.setAttribute('style','border-color: red')
    } else {
        label.setAttribute('style','color: green')
        label.innerHTML = 'Nota da Atividade'
        input.setAttribute('style','border-color: green')
    }
}
function trocarBotao(){
    const cadastrar = document.getElementById('btn-cadastrar');
    const carregando = document.getElementById('btn-loading');

    cadastrar.style.display = 'none';
    carregando.style.display = 'block';
}
function validaData() {
    const labelInicio = document.getElementById('labelInicio');
    const labelFim = document.getElementById('labelFim');
    const inputInicio = document.getElementById('inicio');
    const inputFim = document.getElementById('fim');
    const inf_inicio = inputInicio.value;
    const inf_fim = inputFim.value;

    if (inf_inicio === "" || inf_fim === "") {
        labelFim.style.color = 'blue';
        labelFim.innerHTML = 'Data do Término';
        inputFim.style.borderColor = 'blue';
    } else {
        const inicio = new Date(inf_inicio);
        const fim = new Date(inf_fim);

        if (fim <= inicio) {
            labelInicio.style.color = 'red';
            labelInicio.innerHTML = 'Data de Início * O término não pode ser antes do início';
            inputInicio.style.borderColor = 'red';
            labelFim.style.color = 'red';
            labelFim.innerHTML = 'Data do Término * O término não pode ser antes do início';
            inputFim.style.borderColor = 'red';
        } else {
            labelInicio.style.color = 'green';
            labelInicio.innerHTML = 'Data de Início';
            inputInicio.style.borderColor = 'green';
            labelFim.style.color = 'green';
            labelFim.innerHTML = 'Data do Término';
            inputFim.style.borderColor = 'green';
        }
    }
}
