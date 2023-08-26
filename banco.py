import classes
import mysql.connector
from mysql.connector import Error


# conectando ao banco
try:
    con = mysql.connector.connect(host='localhost', database='mystudyagenda', user='root', password='italo175933')
    cursor = con.cursor()
    conexao = True
except Error as erro:
    print("Erro ao se conectar ao banco de dados: {}".format(erro))
    conexao = False


# função de criação de conta
def cria_conta(conta):
    comando = ("INSERT INTO mystudyagenda.conta(nome, senha, curso, periodo, universidade, notificacaoInterna , notificacaoExterna , nCreditos , email)"
               "VALUE(\'{}\',\'{}\',\'{}\',{},\'{}\',{},{},{},\'{}\')".format(
                conta.nome, conta.senha, conta.curso, conta.periodo, conta.universidade, conta.notificacaoInterna, conta.notificacaoExterna, conta.nCreditos, conta.email))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("erro ao criar conta: {}".format(e))
        saida = False
    return saida


# função de verificação de login
def login(email, senha):
    comando = ("SELECT*FROM mystudyagenda.conta WHERE email = \'{}\' and senha = \'{}\'".format(email, senha))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = False
        else:
            saida = True
    except Error as e:
        print("Erro ao realizar o login: {}".format(e))
        saida = "Erro"
    return saida


# função de criação de materia
def cria_materia(materia):
    comando = ("INSERT INTO mystudyagenda.materia(nome , inicio, fim, nCreditos, nota, observacao, dias, horario, email, estado)"
               "VALUE(\'{}\',{},{},{},{},\'{}\',\'{}\',\'{}\',\'{}\',{})".format(
               materia.nome, materia.inicio, materia.fim, materia.creditos, materia.nota, materia.observacao, materia.dias, materia.horario, materia.email, materia.estado))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("erro ao criar materia: {}".format(e))
        saida = False
    return saida


# função de criação de evento
def cria_evento(evento):
    comando = ("INSERT INTO mystudyagenda.evento(nome , inicio, fim, intervaliInteiro, observacao, estado, horario, lugar, email)"
                "VALUE(\'{}\',{},{},{},\'{}\',{},\'{}\',\'{}\',\'{}\')".format(
                evento.nome, evento.inicio, evento.fim, evento.intervaliInteiro, evento.observacao, evento.estado, evento.horario, evento.lugar, evento.email))

    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("erro ao criar evento: {}".format(e))
        saida = False
    return saida


# função de criação de atividade
def cria_atividade(atividade):
    comando = (
        "INSERT INTO mystudyagenda.atividade(nome , nota, notaAtividade, intervaliInteiro, inicio, fim, horario, estado, observacao, email, nomeMateria, idMateria )"
        "VALUE(\'{}\',{},{},{},{},{},{},{},\'{}\',\'{}\',\'{}\',\'{}\')".format(atividade.nome, atividade.nota, atividade.notaAtividade, atividade.intervaliInteiro, atividade.inicio, atividade.fim, atividade.horario, atividade.estado, atividade.observacao, atividade.email, atividade.nomeMateria, atividade.idMateria))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("erro ao criar atividade: {}".format(e))
        saida = False
    return saida


# função de criação de tarefa
def cria_tarefa(tarefa):
    comando = (
        "INSERT INTO mystudyagenda.tarefas(nome, inicio, fim, intervaliInteiro, horario, lugar, estado, observacao, tipo, email)"
        "VALUE(\'{}\',{},{},{},{},\'{}\',{},\'{}\',\'{}\',\'{}\')".format(
        tarefa.nome, tarefa.inicio, tarefa.fim, tarefa.intervaliInteiro, tarefa.horario, tarefa.lugar, tarefa.estado, tarefa.observacao, tarefa.tipo, tarefa.email))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("erro ao criar tarefa: {}".format(e))
        saida = False
    return saida


# coleta informações da conta
def get_conta(email):
    comando = ("SELECT*FROM mystudyagenda.conta WHERE email = \'{}\'".format(email))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        for linha in linhas:
            saida = classes.Conta(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8])
    except Error as e:
        print("Erro ao coletar informações da conta: {}".format(e))
        saida = "Erro"
    return saida
