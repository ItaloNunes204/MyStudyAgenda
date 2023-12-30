function mostrarCadastros() {
    document.getElementById('cadastros').style.display = 'flex';
}
function fecharCadastros() {
    document.getElementById('cadastros').style.display = 'none';
}
function mostrarConsultas() {
    document.getElementById('consultas').style.display = 'flex';
}
function fecharConsultas() {
    document.getElementById('consultas').style.display = 'none';
}

  document.getElementById('mostrarCadastros').addEventListener('click', mostrarCadastros);
  document.getElementById('fecharCadastros').addEventListener('click', fecharCadastros);
  document.getElementById('mostrarConsultas').addEventListener('click', mostrarConsultas);
  document.getElementById('fecharConsultas').addEventListener('click', fecharConsultas);
