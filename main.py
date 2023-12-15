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
                return redirect("/cadastro_conta")
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


@app.route("/cliente")
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
            if materias == "sem registros" or not materias:
                if not materias:
                    flash("Erro na busca das materias")
                else:
                    flash("Para cadastrar atividades vc deve ter materias cadastradas")
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


@app.route("/consulta")
def consulta():
    if not session.get("name"):
        return redirect("/login")
    else:
        return render_template("consulta.html")


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
                    return redirect("/cliente")
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
                        return render_template("listagemMateria.html", materias=materias)
                    else:
                        return render_template("listagemMateria.html", materias=dados_pesquisa)
        else:
            materias = bd.get_materia(email, True)
            if not materias or materias == "sem registros":
                if not materias:
                    flash("Erro ao coletar as informações")
                    return redirect("/cliente")
                else:
                    return render_template("listagemMateria.html", materias=None)
            else:
                for materia in materias:
                    materia.dias = fr.formata_dias_saida(materia.dias)
                    materia.estado = fr.formata_estado_saida(materia.estado)
                return render_template("listagemMateria.html", materias=materias)


@app.route("/listagem_materia/<id_materia>", methods=["POST", "GET"])
def listagem_materia_apagar(id_materia):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
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

        dados = bd.get_materia_id(email, id_materia)

        if not dados:
            flash("Erro ao coletar as informações")
            return redirect("/cliente")
        else:
            return render_template("listagemMateria.html", materias=materias, dados=dados[0])


@app.route("/apagar_materia/<id_materia>", methods=["POST", "GET"])
def apagar_materia(id_materia):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        materia = bd.get_materia_id(email, id_materia)
        if bd.apagar_materia(materia[0]):
            flash("materia apagada")
        else:
            flash("erro ao apagar a materia")
        return redirect("/listagem_materia")


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
                    return redirect("/cliente")
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
                        return render_template("listagemEvento.html", eventos=eventos)
                    else:
                        return render_template("listagemEvento.html", eventos=dados_pesquisa)
        else:
            eventos = bd.get_evento(email, True)
            if not eventos or eventos == "sem registros":
                if not eventos:
                    flash("Erro ao coletar as informações")
                    return redirect("/cliente")
                else:
                    return render_template("listagemEvento.html", eventos = None)
            else:
                for evento in eventos:
                    evento.estado = fr.formata_estado_saida(evento.estado)
                return render_template("listagemEvento.html", eventos=eventos)


@app.route("/listagem_evento/<id_evento>", methods=["POST", "GET"])
def listagem_evento_apagar(id_evento):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        eventos = bd.get_evento(email, True)
        dados = bd.get_evento_id(email, id_evento)
        if not eventos or eventos == "sem registros":
            if not eventos:
                flash("Erro ao coletar as informações")
            else:
                flash("Sem registros")
            return redirect("/cliente")

        if not dados or dados == "sem registros":
            if not dados:
                flash("Erro ao coletar as informações")
            else:
                flash("Sem registros")
            return redirect("/cliente")
        else:
            for evento in eventos:
                evento.estado = fr.formata_estado_saida(evento.estado)
            return render_template("listagemEvento.html", eventos=eventos, dados=dados[0])


@app.route("/apagar_evento/<id_evento>", methods=["POST", "GET"])
def apagar_evento(id_evento):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        evento = bd.get_evento_id(email, id_evento)
        if bd.apagar_evento(evento[0]):
            flash("evento apagado")
        else:
            flash("erro ao apagar o evento")
        return redirect("/listagem_evento")


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
                    return redirect("/cliente")
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
                    return redirect("/cliente")
                else:
                    return render_template("listagemAtividade.html", atividades=None)
            else:
                for atividade in atividades:
                    atividade.estado = fr.formata_estado_saida(atividade.estado)
                return render_template("listagemAtividade.html", atividades=atividades)


@app.route("/listagem_atividade/<id_atividade>", methods=["POST", "GET"])
def listagem_atividade_apagar(id_atividade):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        atividades = bd.get_atividade(email, True)
        dados = bd.get_atividade_id(email, id_atividade)
        if not atividades or atividades == "sem registros":
            if not atividades:
                flash("Erro ao coletar as informações")
            else:
                flash("Sem registros")
            return redirect("/cliente")

        if not dados or dados == "sem registros":
            if not dados:
                flash("Erro ao coletar as informações")
            else:
                flash("Sem registros")
            return redirect("/cliente")
        else:

            for atividade in atividades:
                atividade.estado = fr.formata_estado_saida(atividade.estado)
            return render_template("listagemAtividade.html", atividades=atividades, dados=dados)


@app.route("/apagar_atividade/<id_atividade>", methods=["POST", "GET"])
def apagar_atividade(id_atividade):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        atividade = bd.get_atividade_id(email, id_atividade)
        if bd.apagar_atividade(atividade[0]):
            flash("atividade apagada")
        else:
            flash("erro ao apagar a atividade")
        return redirect("/listagem_atividade")


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
                    return redirect("/cliente")
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
                    return redirect("/cliente")
                else:
                    return render_template("listagemTarefa.html", tarefas=None)
            else:
                for tarefa in tarefas:
                    tarefa.estado = fr.formata_estado_saida(tarefa.estado)
                return render_template("listagemTarefa.html", tarefas=tarefas)


@app.route("/listagem_tarefa/<id_tarefa>", methods=["POST", "GET"])
def listagem_tarefa_apagar(id_tarefa):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        tarefas = bd.get_tarefas(email, True)
        dados = bd.get_tarefas_id(email, id_tarefa)
        if not tarefas or tarefas == "sem registros":
            if not tarefas:
                flash("Erro ao coletar as informações")
            else:
                flash("Sem registros")
            return redirect("/cliente")

        if not dados or dados == "sem registros":
            if not dados:
                flash("Erro ao coletar as informações")
            else:
                flash("Sem registros")
            return redirect("/cliente")
        else:
            for tarefa in tarefas:
                    tarefa.estado = fr.formata_estado_saida(tarefa.estado)
            return render_template("listagemTarefa.html", tarefas=tarefas, dados=dados)


@app.route("/apagar_tarefa/<id_tarefa>", methods=["POST", "GET"])
def apagar_tarefa(id_tarefa):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        tarefas = bd.get_tarefa_id(email, id_tarefa)
        if bd.apagar_tarefa(tarefas[0]):
            flash("tarefa apagada")
        else:
            flash("erro ao apagar a tarefa")
        return redirect("/listagem_tarefa")


@app.route("/modifica_conta", methods=["POST", "GET"])
def modifica_conta():
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            nome = request.form.get("nome")
            senha = request.form.get("senha")
            conf_senha = request.form.get("confsenha")
            curso = request.form.get("curso")
            periodo = request.form.get("periodo")
            universidade = request.form.get("universidade")
            conta = bd.get_conta(email)
            if senha != "":
                if senha != conf_senha:
                    flash("senhas incompativeis")
                    return redirect("/modifica_conta")
                else:
                    conta.senha = fr.codificando(senha)
            conta.nome = nome
            conta.curso = curso
            conta.periodo = periodo
            conta.universidade = universidade
            if bd.modifica_conta(conta):
                flash("Conta modificada")
                return redirect("/cliente")
            else:
                flash("Erro ao modificar a conta")
                return redirect("/modifica_conta")
        else:
            conta = bd.get_conta(email)
            return render_template("modificaConta.html", conta=conta)


@app.route("/modifica_materia/<id_materia>", methods=["POST", "GET"])
def modifica_materia(id_materia):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
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
                flash("Informe os dias")
                return redirect("/modifica_materia/{}".format(id_materia))
            else:
                dia = fr.formata_dias(dias)
                materia = bd.get_materia_id(email, id_materia)
                materia = materia[0]
                materia.nome = nome
                materia.inicio = inicio
                materia.fim = fim
                materia.horario = horario
                materia.creditos = creditos
                materia.observacao = observacao
                materia.dias = dia
                if bd.modifica_materia(materia):
                    flash("materia modificada")
                    return redirect("/cliente")
                else:
                    flash("Erro ao modificar a materia")
                    return redirect("/modifica_materia/{}".format(id_materia))
        else:
            materia = bd.get_materia_id(email, id_materia)
            materia[0].horario = fr.formata_hora_modifica(materia[0].horario)
            dias = fr.formata_dias_modifica_materia(materia[0].dias)
            return render_template("modificaMateria.html", materia=materia[0], dias=dias)


@app.route("/modifica_tarefa/<id_tarefa>", methods=["POST", "GET"])
def modifica_tarefa(id_tarefa):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            nome = request.form.get("nome")
            inicio = request.form.get("inicio")
            fim = request.form.get("fim")
            intervalo = request.form.get("intervalo")
            if intervalo == "on":
                intervalo = True
            else:
                intervalo = False
            horario = request.form.get("horario")
            lugar = request.form.get("lugar")
            observacao = request.form.get("observacao")
            tipo = request.form.get("tipo")

            tarefa = bd.get_tarefas_id(email, id_tarefa)
            tarefa.nome = nome
            tarefa.inicio = inicio
            tarefa.fim = fim
            tarefa.intervalo = intervalo
            tarefa.horario = horario
            tarefa.lugar = lugar
            tarefa.observacao = observacao
            tarefa.tipo = tipo
            if not bd.modifica_tarefa(tarefa):
                flash("erro ao modificar a tarefa")
                return redirect("/modifica_tarefa/{}".format(id_tarefa))

        else:
            tarefa = bd.get_tarefas_id(email, id_tarefa)
            return render_template("modificaTarefas.html", tarefa=tarefa)


@app.route("/modifica_atividade/<id_atividade>", methods=["POST", "GET"])
def modifica_atividade(id_atividade):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            nome = request.form.get("nome")
            inicio = request.form.get("inicio")
            fim = request.form.get("fim")
            intervalo = request.form.get("intervalo")
            if intervalo == "on":
                intervalo = True
            else:
                intervalo = False
            horario = request.form.get("horario")
            nota_atividade = request.form.get("nota_atividade")
            nota = request.form.get("nota")
            nome_atividade = request.form.get("materia")
            observacao = request.form.get("observacao")
            id_materia = None
            materias = bd.get_materia(email, True)
            for materia in materias:
                if materia.nome == nome_atividade:
                    id_materia = materia.idMateria
                    break
            if id_materia is None:
                materias = bd.get_materia(email, False)
                for materia in materias:
                    if materia.nome == nome_atividade:
                        id_materia = materia.idMateria
                        break
            atividade = bd.get_atividade_id(email, id_atividade)
            atividade.nome = nome
            atividade.inicio = inicio
            atividade.fim = fim
            atividade.intervalo = intervalo
            atividade.horario = horario
            atividade.notaAtividade = nota_atividade
            atividade.nota = nota
            atividade.nomeMateria = nome_atividade
            atividade.idMateria = id_materia
            if not bd.modifica_atividade(atividade):
                flash("erro ao modificar a atividade")
                return redirect("/modifica_atividade/{}".format(id_atividade))
        else:
            atividade = bd.get_atividade_id(email, id_atividade)
            return render_template("modificaAtividade.html", atividade=atividade)


@app.route("/modifica_evento/<id_evento>", methods=["POST", "GET"])
def modifica_evento(id_evento):
    if not session.get("name"):
        return redirect("/login")
    else:
        email = session.get("name")
        if request.method == "POST":
            nome = request.form.get("nome")
            inicio = request.form.get("inicio")
            fim = request.form.get("fim")
            intervalo = request.form.get("intervalo")
            if intervalo == "on":
                intervalo = True
            else:
                intervalo = False
            horario = request.form.get("horario")
            lugar = request.form.get("lugar")
            observacao = request.form.get("observacao")

            evento = bd.get_evento_id(email, id_evento)
            evento = evento[0]
            evento.nome = nome
            evento.inicio = inicio
            evento.fim = fim
            evento.intervalo = intervalo
            evento.horario = horario
            evento.lugar = lugar
            evento.observacao = observacao
            if not bd.modifica_evento(evento):
                flash("erro ao modificar evento")
                return redirect("/modifica_evento/{}".format(id_evento))
            else:
                flash("evento modificado")
                return redirect("/listagem_evento")
        else:
            eventos = bd.get_evento_id(email, id_evento)
            eventos[0].horario = fr.formata_hora_modifica(eventos[0].horario)
            return render_template("modificaEvento.html", evento=eventos[0])


if __name__ == "__main__":
    app.run(debug=True)
