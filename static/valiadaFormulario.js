function validaAtividade(){
    var cores = true;
    const nome = document.getElementById('labelNome');
    if(window.getComputedStyle(nome).getPropertyValue('color')!=="rgb(0, 128, 0)"){
        cores = false
    }
    const inicio = document.getElementById('labelInicio');
    if(window.getComputedStyle(inicio).getPropertyValue('color')!=="rgb(0, 128, 0)"){
        cores = false
    }
    const fim = document.getElementById('labelFim');
    if(window.getComputedStyle(fim).getPropertyValue('color')!=="rgb(0, 128, 0)"){
        cores = false
    }
    const hora = document.getElementById('labelHorario');
    if(window.getComputedStyle(hora).getPropertyValue('color')!=="rgb(0, 128, 0)"){
        cores = false
    }
    const nota = document.getElementById('labelNota');
    if(window.getComputedStyle(nota).getPropertyValue('color')!=="rgb(0, 128, 0)"){
        cores = false
    }
    //var materia = document.getElementById('materia');
    //cores.push(window.getComputedStyle(materia).getPropertyValue('border-color'));
    const observacao = document.getElementById('labelObservacao');
    if(window.getComputedStyle(observacao).getPropertyValue('color')!=="rgb(0, 128, 0)"){
        cores = false
    }
    const botao = document.getElementById('btn-cadastrar');
    if(cores == true){
        botao.style.display = 'block';
    }else{
        botao.style.display = 'none';
    }
}
