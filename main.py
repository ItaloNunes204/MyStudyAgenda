from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
import formatador as fr
import classes
import banco as bd


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "teste_palavra_chave"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro_conta", methods=["POST", "GET"])
def cadastro_conta():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        conf_senha = request.form.get("confsenha")
        curso = request.form.get("curso")
        periodo = request.form.get("periodo")
        universidade = request.form.get("universidade")
        if senha != conf_senha:
            flash("As senhas não conferem")
            return redirect("/cadastro_conta")
        else:
            senha = fr.codificando(senha)
            conta = classes.Conta(nome, senha, curso, periodo, universidade, True, True, 0, email)
            if bd.cria_conta(conta):
                session["name"] = email
                return redirect('/cliente')
            else:
                flash("Erro ao cadastrar a conta")
    else:
        return render_template("cadastroConta.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        senha = fr.codificando(senha)
        if bd.login(email, senha):
            session["name"] = email
            return redirect('/cliente')
        else:
            flash("Conta invalida")
            return redirect('/login')
    else:
        return render_template("login.html")


@app.route('/cliente')
def cliente():
    if not session.get("name"):
        return redirect("/login")
    else:
        return render_template("inicio.html")


@app.route("/sair")
def sair():
    session["name"] = None
    return redirect("/")


@app.route("/cadastro_materias", methods=["POST", "GET"])
def cadastro_materias():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            email = session.get("name")
            nome = request.form.get("nome")
            inicio = request.form.get("inicio")
            fim = request.form.get("fim")
            horario = request.form.get("horario")
            creditos = request.form.get("creditos")
            observacao = request.form.get("observacao")

            segunda = request.form.get("segunda")
            terca = request.form.get("terca")
            quarta = request.form.get("quarta")
            quinta = request.form.get("quinta")
            sexta = request.form.get("sexta")
            sabado = request.form.get("sabado")
            dias = []
            if segunda == 'on':
                dias.append("Segunda")
            if terca == 'on':
                dias.append("Terça")
            if quarta == 'on':
                dias.append("Quarta")
            if quinta == 'on':
                dias.append("Quinta")
            if sexta == 'on':
                dias.append("Sexta")
            if sabado == 'on':
                dias.append("Sabado")
            if len(dias) == 0:
                flash("Informe os dias da materia")
                return redirect("/cadastro_materias")
            else:
                dias = fr.formata_dias(dias)
                inicio = fr.troca_tipo_data(inicio)
                fim = fr.troca_tipo_data(fim)
                horario = fr.troca_tipo_hora(horario)
                nova_materia = classes.Materia(nome, inicio, fim, creditos, 0, observacao,
                                               dias, horario, email, True, None)
                if bd.cria_materia(nova_materia):
                    flash("Materia cadastrada")
                    return redirect("/cliente")
                else:
                    flash("Erro ao cadastrar a materia")
                    return redirect("/cadastro_materias")
        else:
            return render_template("cadastroMateria.html")


@app.route("/cadastro_eventos", methods=["POST", "GET"])
def cadastro_eventos():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            email = session.get("name")
            nome = request.form.get("nome")
            inicio = request.form.get("inicio")
            fim = request.form.get("fim")
            intervalo = request.form.get("intervalo")
            horario = request.form.get("horario")
            lugar = request.form.get("lugar")
            observacao = request.form.get("observacao")
            if intervalo == "on":
                intervalo = True
            else:
                intervalo = False
            inicio = fr.troca_tipo_data(inicio)
            fim = fr.troca_tipo_data(fim)
            horario = fr.troca_tipo_hora(horario)
            novo_evento = classes.Evento(nome, inicio, fim, intervalo, observacao, True, horario, lugar, email, None)
            if bd.cria_evento(novo_evento):
                flash("Evento Cadastrado")
                return redirect("/cliente")
            else:
                flash("Erro ao cadastrar o evento")
                return redirect("/cadastro_eventos")
        else:
            return render_template("cadastroEvento.html")


@app.route("/cadastro_atividades", methods=["POST", "GET"])
def cadastro_atividades():
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            nome = request.form.get("nome")
            inicio = request.form.get("inicio")
            fim = request.form.get("fim")
            intervalo = request.form.get("intervalo")
            horario = request.form.get("horario")
            nota_atividade = request.form.get("nota")
            nome_materia = request.form.get("materia")
            observacao = request.form.get("observacao")
            materias = bd.get_materia(email, True)
            id_materia = 0
            if not materias or materias == "sem registros":
                flash("Erro na busca das materias")
                return redirect("/cliente")
            else:
                for materia in materias:
                    if fr.formata_nome(materia.nome) == nome_materia:
                        id_materia = materia.idMateria
                        break
            if intervalo == "on":
                intervalo = True
            else:
                intervalo = False
            inicio = fr.troca_tipo_data(inicio)
            fim = fr.troca_tipo_data(fim)
            horario = fr.troca_tipo_hora(horario)
            nova_atividade = classes.Atividade(nome, 0, nota_atividade, intervalo, inicio, fim,
                                               horario, True, observacao, email, nome_materia, id_materia, None)
            if bd.cria_atividade(nova_atividade):
                flash("Atividade cadastrada")
                return redirect("/cliente")
            else:
                flash("Erro ao cadastrar a atividade")
                return redirect("/cadastro_atividades")
        else:
            materias = bd.get_materia(email, True)
            if materias == "sem registros":
                flash("Para cadastrar atividades vc deve ter materias cadastradas")
                return redirect("/cliente")
            else:
                if not materias:
                    flash("Erro na busca das materias")
                    return redirect("/cliente")
                else:
                    for materia in materias:
                        materia.nome = fr.formata_nome(materia.nome)
                    return render_template("cadastroAtividade.html", materias=materias)


@app.route("/cadastro_tarefas", methods=["POST", "GET"])
def cadastro_tarefas():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            email = session.get("name")
            nome = request.form.get("nome")
            inicio = request.form.get("inicio")
            fim = request.form.get("fim")
            intervalo = request.form.get("intervalo")
            horario = request.form.get("horario")
            lugar = request.form.get("lugar")
            observacao = request.form.get("observacao")
            tipo = request.form.get("tipo")
            if intervalo == "on":
                intervalo = True
            else:
                intervalo = False
            inicio = fr.troca_tipo_data(inicio)
            fim = fr.troca_tipo_data(fim)
            horario = fr.troca_tipo_hora(horario)
            nova_tarefa = classes.Tarefa(nome, inicio, fim, intervalo, horario, lugar, True,
                                         observacao, tipo, email, None)
            if bd.cria_tarefa(nova_tarefa):
                flash("Tarefa cadastrada")
                return redirect("/cliente")
            else:
                flash("Erro ao cadastrar a tarefa")
                return redirect("/cadastro_tarefas")
        else:
            return render_template("cadastroTarefas.html")


@app.route("/listagem_materia", methods=["POST", "GET"])
def listagem_materia():
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            pesquisa = request.form.get("pesquisa")
            antigos = request.form.get("antigos")
            if antigos == "on":
                antigos = False
            else:
                antigos = True
            materias = bd.get_materia(email, antigos)
            if not materias or materias == "sem registros":
                if not materias:
                    flash("Erro ao coletar as informações")
                else:
                    flash("Sem registros")
                return redirect("/listagem_materia")
            else:
                for materia in materias:
                    materia.dias = fr.formata_dias_saida(materia.dias)
                    materia.estado = fr.formata_estado_saida(materia.estado)

                if pesquisa == "":
                    return render_template("listagemMateria.html", materias=materias)
                else:
                    dados_pesquisa = []
                    for materia in materias:
                        dado = pesquisa in materia.nome
                        if dado:
                            dados_pesquisa.append(materia)
                    if len(dados_pesquisa) == 0:
                        flash("Pesquisa não encontrada")
                        return redirect("/listagem_materia")
                    else:
                        return render_template("listagemMateria.html", materias=dados_pesquisa)
        else:
            materias = bd.get_materia(email, True)
            if not materias or materias == "sem registros":
                if not materias:
                    flash("Erro ao coletar as informações")
                else:
                    flash("Sem registros")
                return redirect("/cliente")
            else:
                for materia in materias:
                    materia.dias = fr.formata_dias_saida(materia.dias)
                    materia.estado = fr.formata_estado_saida(materia.estado)
                return render_template("listagemMateria.html", materias=materias)


@app.route("/listagem_evento", methods=["POST", "GET"])
def listagem_evento():
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            pesquisa = request.form.get("pesquisa")
            antigos = request.form.get("antigos")
            if antigos == "on":
                antigos = False
            else:
                antigos = True
            eventos = bd.get_evento(email, antigos)
            if not eventos or eventos == "sem registros":
                if not eventos:
                    flash("Erro ao coletar as informações")
                else:
                    flash("Sem registros")
                return redirect("/listagem_evento")
            else:
                for evento in eventos:
                    evento.estado = fr.formata_estado_saida(evento.estado)

                if pesquisa == "":
                    return render_template("listagemEvento.html", eventos=eventos)
                else:
                    dados_pesquisa = []
                    for evento in eventos:
                        dado = pesquisa in evento.nome
                        if dado:
                            dados_pesquisa.append(evento)
                    if len(dados_pesquisa) == 0:
                        flash("Pesquisa não encontrada")
                        return redirect("/listagem_evento")
                    else:
                        return render_template("listagemEvento.html", eventos=dados_pesquisa)
        else:
            eventos = bd.get_evento(email, True)
            if not eventos or eventos == "sem registros":
                if not eventos:
                    flash("Erro ao coletar as informações")
                else:
                    flash("Sem registros")
                return redirect("/cliente")
            else:
                for evento in eventos:
                    evento.estado = fr.formata_estado_saida(evento.estado)
                return render_template("listagemMateria.html", eventos=eventos)


@app.route("/listagem_atividade", methods=["POST", "GET"])
def listagem_atividades():
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            pesquisa = request.form.get("pesquisa")
            antigos = request.form.get("antigos")
            if antigos == "on":
                antigos = False
            else:
                antigos = True
            atividades = bd.get_atividade(email, antigos)
            if not atividades or atividades == "sem registros":
                if not atividades:
                    flash("Erro ao coletar as informações")
                else:
                    flash("Sem registros")
                return redirect("/listagem_atividades")
            else:
                for atividade in atividades:
                    atividade.estado = fr.formata_estado_saida(atividade.estado)

                if pesquisa == "":
                    return render_template("listagemAtividade.html", atividades=atividades)
                else:
                    dados_pesquisa = []
                    for atividade in atividades:
                        dado = pesquisa in atividade.nome
                        if dado:
                            dados_pesquisa.append(atividade)
                    if len(dados_pesquisa) == 0:
                        flash("Pesquisa não encontrada")
                        return redirect("/listagem_atividade")
                    else:
                        return render_template("listagemAtividade.html", atividades=dados_pesquisa)
        else:
            atividades = bd.get_atividade(email, True)
            if not atividades or atividades == "sem registros":
                if not atividades:
                    flash("Erro ao coletar as informações")
                else:
                    flash("Sem registros")
                return redirect("/cliente")
            else:
                for atividade in atividades:
                    atividade.estado = fr.formata_estado_saida(atividade.estado)
                return render_template("listagemAtividade.html", atividades=atividades)


@app.route("/listagem_tarefa", methods=["POST", "GET"])
def listagem_tarefa():
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            pesquisa = request.form.get("pesquisa")
            antigos = request.form.get("antigos")
            if antigos == "on":
                antigos = False
            else:
                antigos = True
            tarefas = bd.get_tarefas(email, antigos)
            if not tarefas or tarefas == "sem registros":
                if not tarefas:
                    flash("Erro ao coletar as informações")
                else:
                    flash("Sem registros")
                return redirect("/listagem_tarefa")
            else:
                for tarefa in tarefas:
                    tarefa.estado = fr.formata_estado_saida(tarefa.estado)

                if pesquisa == "":
                    return render_template("listagemTarefa.html", tarefas=tarefas)
                else:
                    dados_pesquisa = []
                    for tarefa in tarefas:
                        dado = pesquisa in tarefa.nome
                        if dado:
                            dados_pesquisa.append(tarefa)
                    if len(dados_pesquisa) == 0:
                        flash("Pesquisa não encontrada")
                        return redirect("/listagem_tarefa")
                    else:
                        return render_template("listagemTarefa.html", tarefas=dados_pesquisa)
        else:
            tarefas = bd.get_tarefas(email, True)
            if not tarefas or tarefas == "sem registros":
                if not tarefas:
                    flash("Erro ao coletar as informações")
                else:
                    flash("Sem registros")
                return redirect("/cliente")
            else:
                for tarefa in tarefas:
                    tarefa.estado = fr.formata_estado_saida(tarefa.estado)
                return render_template("listagemTarefa.html", tarefas=tarefas)


if __name__ == "__main__":
    app.run(debug=True)
