function validaAtividade(){
    const cores = [];
    const nome = document.getElementById('labelNome');
    cores.push(window.getComputedStyle(nome).getPropertyValue('color'));
    const inicio = document.getElementById('labelInicio');
    cores.push(window.getComputedStyle(inicio).getPropertyValue('color'));
    const fim = document.getElementById('labelFim');
    cores.push(window.getComputedStyle(fim).getPropertyValue('color'));
    const hora = document.getElementById('labelHorario');
    cores.push(window.getComputedStyle(hora).getPropertyValue('color'));
    const nota = document.getElementById('labelNota');
    cores.push(window.getComputedStyle(nota).getPropertyValue('color'));
    //var materia = document.getElementById('materia');
    //cores.push(window.getComputedStyle(materia).getPropertyValue('border-color'));
    const observacao = document.getElementById('labelObservacao');
    cores.push(window.getComputedStyle(observacao).getPropertyValue('color'));
    let contador = 0;
    for(var i = 0; i < cores.length;i++){
        if(cores[i] === "rgb(0, 128, 0)"){
            contador++;
        }
    }
    alert("a quantidade de campos validos e: " + contador);
    const botao = document.getElementById('btn-cadastrar');
    if(contador === cores.length){
        botao.style.display = 'block';
    }else{
        botao.style.display = 'none';
    }
}
