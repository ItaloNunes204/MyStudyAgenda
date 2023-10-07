import hashlib
import datetime


# aplica a criptografia MD5 na senha.
def codificando(senha):
    result = hashlib.md5(senha.encode())
    return str(result.hexdigest())


def formata_dias(dias):
    saida = "dias"
    for dia in dias:
        saida = saida + "," + str(dia)
    return saida


def troca_tipo_data(data):
    saida = datetime.datetime.strptime(data, '%Y-%m-%d')
    return saida


def troca_tipo_hora(hora):
    saida = datetime.datetime.strptime(hora, '%H:%M')
    return saida


def formata_nome(nome):
    saida = nome.replace(' ', '_')
    return saida


def formata_dias_saida(dias):
    saida = dias.replace('dias,', '')
    return saida


def formata_estado_saida(estado):
    if estado == 1:
        saida = "cursando"
    else:
        saida = "Finalizado"
    return saida


def formata_dias_modifica_materia(dias_entrada):
    dias = [0,0,0,0,0,0]
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
