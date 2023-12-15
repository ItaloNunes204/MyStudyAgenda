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
    comando = ("INSERT INTO mystudyagenda.conta(nome, senha, curso, periodo, universidade, notificacaoInterna, notificacaoExterna, nCreditos, email)"
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
    comando = ("INSERT INTO mystudyagenda.materia(nome, inicio, fim, nCreditos, nota, observacao, dias, horario, email, estado)"
               "VALUE(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',{})".format(materia.nome, materia.inicio, materia.fim, materia.creditos, materia.nota, materia.observacao, materia.dias, materia.horario, materia.email, materia.estado))
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
    comando = ("INSERT INTO mystudyagenda.evento(nome, inicio, fim, intervaliInteiro, observacao, estado, horario, lugar, email)VALUE(\'{}\',\'{}\',\'{}\',{},\'{}\',{},\'{}\',\'{}\',\'{}\')".format(evento.nome, evento.inicio, evento.fim, evento.intervalo, evento.observacao, evento.estado, evento.horario, evento.lugar, evento.email))

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
        "INSERT INTO mystudyagenda.atividade(nome, nota, notaAtividade, intervaliInteiro, inicio, fim, horario, estado, observacao, email, nomeMateria, idMateria )"
        "VALUE(\'{}\',\'{}\',\'{}\',{},\'{}\',\'{}\',\'{}\',{},\'{}\',\'{}\',\'{}\',\'{}\')".format(atividade.nome, atividade.nota, atividade.notaAtividade, atividade.intervalo, atividade.inicio, atividade.fim, atividade.horario, atividade.estado, atividade.observacao, atividade.email, atividade.nomeMateria, atividade.idMateria))
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
    comando = ("INSERT INTO mystudyagenda.tarefas(nome, inicio, fim, intervaliInteiro, horario, lugar, estado, observacao, tipo, email)VALUE(\'{}\',\'{}\',\'{}\',{},\'{}\',\'{}\',{},\'{}\',\'{}\',\'{}\')".format(
               tarefa.nome, tarefa.inicio, tarefa.fim, tarefa.intervalo, tarefa.horario, tarefa.lugar, tarefa.estado, tarefa.observacao, tarefa.tipo, tarefa.email))
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
        linha = linhas[0]
        saida = classes.Conta(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8])
    except Error as e:
        print("Erro ao coletar informações da conta: {}".format(e))
        saida = False
    return saida


# coleta todas as materias
def get_materia(email, estado):
    comando = ("SELECT*FROM mystudyagenda.materia WHERE email = \'{}\' and estado = {}".format(email, estado))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(classes.Materia(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10]))
    except Error as e:
        print("Erro ao coletar as materias: {}".format(e))
        saida = False
    return saida


# coleta todas as atividades
def get_atividade(email, estado):
    comando = ("SELECT*FROM mystudyagenda.atividade WHERE email = \'{}\' and estado = {}".format(email, estado))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(classes.Atividade(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12]))
    except Error as e:
        print("Erro ao coletar as atividades: {}".format(e))
        saida = False
    return saida


# coleta todos os eventos
def get_evento(email, estado):
    comando = ("SELECT*FROM mystudyagenda.evento WHERE email = \'{}\' and estado = {}".format(email, estado))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(
                    classes.Evento(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7],
                                   linha[8], linha[9]))
    except Error as e:
        print("Erro ao coletar as atividades: {}".format(e))
        saida = False
    return saida


# coleta todas as tarefas
def get_tarefas(email, estado):
    comando = ("SELECT*FROM mystudyagenda.tarefas WHERE email = \'{}\' and estado = {}".format(email, estado))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(
                    classes.Tarefa(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10]))
    except Error as e:
        print("Erro ao coletar as tarefas: {}".format(e))
        saida = False
    return saida


# modifica conta
def modifica_conta(conta):
    comando = ("UPDATE mystudyagenda.conta SET nome = \'{}\', senha = \'{}\', curso = \'{}\',periodo = {} ,"
               "universidade = \'{}\',notificacaoInterna = {},notificacaoExterna = {},nCreditos = {}  WHERE email = \'{}\'".format(
                conta.nome, conta.senha, conta.curso, conta.periodo, conta.universidade, conta.notificacaoInterna, conta.notificacaoExterna, conta.nCreditos, conta.email))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao modificar a conta: {}".format(e))
        saida = False
    return saida


# modifica evento
def modifica_evento(evento):
    comando = ("UPDATE mystudyagenda.evento SET nome = \'{}\',inicio = \'{}\',fim = \'{}\' ,intervaliInteiro = {},observacao = \'{}\',estado = {},horario = \'{}\',Lugar = \'{}\' WHERE email = \'{}\' and idEvento = \'{}\'".format(
        evento.nome, evento.inicio, evento.fim, evento.intervalo, evento.observacao, evento.estado, evento.horario, evento.lugar, evento.email, evento.idEvento))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao modificar o evento: {}".format(e))
        saida = False
    return saida


# modifica atividade
def modifica_atividade(atividade):
    comando = (
        " UPDATE mystudyagenda.atividade SET nome = \'{}\', nota = \'{}\', notaAtividade = \'{}\', intervaliInteiro = {}, inicio = \'{}\', "
        "fim = \'{}\', horario = \'{}\', estado = {}, observacao = \'{}\', nomeMateria = \'{}\' WHERE email = \'{}\' and id_atividade = {}".format(atividade.nome, atividade.nota, atividade.notaAtividade, atividade.intervalo, atividade.inicio, atividade.fim, atividade.horario, atividade.estado, atividade.observacao, atividade.nomeMateria, atividade.email, atividade.idAtividade))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao modificar a atividade: {}".format(e))
        saida = False
    return saida


# modifica materia
def modifica_materia(materia):
    comando = (
        " UPDATE mystudyagenda.materia SET nome = \'{}\' , inicio = \'{}\', fim = \'{}\', nCreditos = \'{}\', nota = \'{}\', observacao = \'{}\', "
        "dias = \'{}\', horario = \'{}\', estado = {} WHERE email = \'{}\' and idMateria = \'{}\'".format(materia.nome, materia.inicio, materia.fim, materia.creditos, materia.nota, materia.observacao, materia.dias, materia.horario, materia.estado, materia.email, materia.idMateria))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao modificar o evento: {}".format(e))
        saida = False
    return saida


# modifica tarefas
def modifica_tarefa(tarefa):
    comando = (
        " UPDATE mystudyagenda.tarefas SET nome = \'{}\', inicio = \'{}\', fim = \'{}\', intervaliInteiro = {}, horario = \'{}\', lugar = \'{}\', estado = {}, observacao = \'{}\',"
        "tipo = \'{}\' WHERE email = \'{}\' and idTarefa = \'{}\'".format(tarefa.nome, tarefa.inicio, tarefa.fim, tarefa.intervalo, tarefa.horario, tarefa.lugar, tarefa.estado, tarefa.observacao, tarefa.tipo, tarefa.email, tarefa.idTarefa))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao modificar o evento: {}".format(e))
        saida = False
    return saida


# coleta o evento com o id
def get_evento_id(email, id_evento):
    comando = ("SELECT*FROM mystudyagenda.evento WHERE email = \'{}\' and idEvento = {}".format(email, id_evento))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(
                    classes.Evento(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7],
                                   linha[8], linha[9]))
    except Error as e:
        print("Erro ao coletar as atividades: {}".format(e))
        saida = False
    return saida


# coleta a atividade com o id
def get_atividade_id(email, id_atividade):
    comando = ("SELECT*FROM mystudyagenda.atividade WHERE email = \'{}\' and idAtividade = {}".format(email, id_atividade))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(classes.Atividade(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12]))
    except Error as e:
        print("Erro ao coletar as atividades: {}".format(e))
        saida = False
    return saida


# coleta a tarefa  com o id
def get_tarefas_id(email, id_tarefa):
    comando = ("SELECT*FROM mystudyagenda.tarefas WHERE email = \'{}\' and idTarefa = {}".format(email, id_tarefa))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(
                    classes.Tarefa(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10]))
    except Error as e:
        print("Erro ao coletar as tarefas: {}".format(e))
        saida = False
    return saida


# coleta a materia  com o id
def get_materia_id(email, id_materia):
    comando = ("SELECT*FROM mystudyagenda.materia WHERE email = \'{}\' and idMateria = {}".format(email, id_materia))
    try:
        cursor.execute(comando)
        linhas = cursor.fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(classes.Materia(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10]))
    except Error as e:
        print("Erro ao coletar as materias: {}".format(e))
        saida = False
    return saida


# apaga a materia do banco
def apagar_materia(materia):
    comando = ("DELETE FROM mystudyagenda.materia WHERE idMateria = {}".format(materia.idMateria))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao apagar a materia: {}".format(e))
        saida = False
    return saida


# apaga a atividade do banco
def apagar_atividade(atividade):
    comando = ("DELETE FROM mystudyagenda.atividade WHERE id_atividade = {}".format(atividade.idAtividade))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao apagar a atividade: {}".format(e))
        saida = False
    return saida


# apaga o evento do banco
def apagar_evento(evento):
    comando = ("DELETE FROM mystudyagenda.evento WHERE idEvento = {}".format(evento.idEvento))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao apagar a evento: {}".format(e))
        saida = False
    return saida


# apaga a tarefa do banco
def apagar_tarefa(tarefa):
    comando = ("DELETE FROM mystudyagenda.tarefas WHERE idTarefa = {}".format(tarefa.idTarefa))
    try:
        cursor.execute(comando)
        con.commit()
        saida = True
    except Error as e:
        print("Erro ao apagar a tarefa: {}".format(e))
        saida = False
    return saida
