import hashlib
import datetime


# aplica a criptografia MD5 na senha.
def codificando(senha):
    result = hashlib.md5(senha.encode())
    return str(result.hexdigest())


# transforma uma lista de dias em uma unica string
def formata_dias(dias):
    saida = "dias"
    for dia in dias:
        saida = saida + "," + str(dia)
    return saida


# transforma uma string em uma variavel do tipo datetime,"date"
def troca_tipo_data(data):
    saida = datetime.datetime.strptime(data, '%Y-%m-%d')
    return saida


# transforma uma string em uma variavel do tipo datetime,"time"
def troca_tipo_hora(hora):
    saida = datetime.datetime.strptime(hora, '%H:%M')
    return saida


# troca os espaços por um _
def formata_nome(nome):
    saida = nome.replace(' ', '_')
    return saida


# tira uma parte da string "dias,"
def formata_dias_saida(dias):
    saida = dias.replace('dias,', '')
    return saida


# troca variaveis booleanas por strings para serem exibidas
def formata_estado_saida(estado):
    if estado == 1:
        saida = "cursando"
    else:
        saida = "Finalizado"
    return saida


# cria um vetor que armazena 1 ou 0 para cada dia da semana
def formata_dias_modifica_materia(dias_entrada):
    dias = [0, 0, 0, 0, 0, 0]
    saidas = dias_entrada.replace('dias,', '')
    saidas = saidas.split(',')
    for saida in saidas:
        if saida == "Segunda":
            dias[0] = 1
        else:
            if saida == "Terça":
                dias[1] = 1
            else:
                if saida == "Quarta":
                    dias[2] = 1
                else:
                    if saida == "Quinta":
                        dias[3] = 1
                    else:
                        if saida == "Sexta":
                            dias[4] = 1
                        else:
                            if saida == "Sabado":
                                dias[5] = 1
    return dias


# transforma uma variavel datetime em uma string
def formata_hora_modifica(hora):
    hora = str(hora)
    dados = hora.split(":")
    if int(dados[0]) < 10:
        dados[0] = "0" + dados[0]
    saida = dados[0] + ":" + dados[1]
    return saida
