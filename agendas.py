import classes as cl
import banco as bd
import datetime
import calendar
import formatador as fr


def cria_descricao(tipo,nome,dia,hora):
    descricao = dia + " " + hora + " você tem: " + tipo + " " + nome
    return descricao


def adiciona_descricao(descricao,tipo,nome):
    nova_descricao = descricao + ", " + tipo + nome
    return nova_descricao


def cria_assunto(hora,dia,observacao):
    assunto = dia + " " + hora + " - " + observacao
    return assunto


def busca_segunda(dia):
    if dia.weekday() != 0:
        dia -= datetime.timedelta(days=dia.weekday())
    return dia


def coleta_informacao_materia(email, dia):
    materias = bd.get_all_materia(email)
    if materias != False or materias != 'sem registros':
        materias_validas = []
        for materia in materias:
            if dia <= materia.fim:
                materias_validas.append(materia)
        return materias_validas
    else:
        return False


def coleta_informacao_atividades(email, dia_validacao):
    atividades = bd.get_all_atividades(email)
    if atividades != False or atividades != "sem registros":
        atividades_validas = []
        for atividade in atividades:
            if dia_validacao <= atividade.fim:
                atividades_validas.append(atividade)
        return atividades_validas
    else:
        return False


def coleta_informacao_eventos(email, dia_validacao):
    eventos = bd.get_all_eventos(email)
    if eventos == False or eventos == 'sem registros':
        return False
    else:
        eventos_validos = []
        for evento in eventos:
            if dia_validacao <= evento.fim:
                eventos_validos.append(evento)
        return eventos_validos


def coleta_informacao_tarefas(email, dia_validacao):
    tarefas = bd.get_all_tarefas(email)
    if tarefas != False or tarefas != "sem registros":
        tarefas_validas = []
        for tarefa in tarefas:
            if dia_validacao <= tarefa.fim:
                tarefas_validas.append(tarefa)
        return tarefas_validas
    else:
        return False


def converte_dia(dia):
    if dia == 0:
        return "Segunda"
    else: 
        if dia == 1:
            return "Terça"
        else:
            if dia == 2:
                return "Quarta"
            else:
                if dia == 3:
                    return "Quinta"
                else:
                    if dia == 4:
                        return "Sexta"
                    else:
                        if dia == 5:
                            return "Sabado"
                        else:
                            return "Domindo"


def completa_descricao(mes, ano, email, calendario):
    dia = datetime.date(ano, mes, 1)
    materias = coleta_informacao_materia(email,dia)
    atividades = coleta_informacao_atividades(email, dia)
    eventos = coleta_informacao_eventos(email, dia)
    tarefas = coleta_informacao_tarefas(email, dia)
    
    if materias == False or atividades == False or eventos == False or tarefas == False:
        return False
    else:
        for data in calendario:
            if data.dia == "---":
                pass
            else:
                for materia in materias:
                    verificador_dia = datetime.date(ano, mes, int(data.dia))
                    if materia.fim >= verificador_dia:
                        dias = fr.formata_dias_saida(materia.dias)
                        dias = dias.split(',')
                        verificador = False
                        for dia in dias:
                            if dia.lower() == data.diaS.lower():
                                verificador = True
                                break
                        if materia.fim == datetime.datetime(ano, mes, data.dia):
                            if verificador == True:
                                data.descricao += "[temino da materia: {} tem aula: {}]".format(materia.nome,materia.nome)
                            else:
                                data.descricao += "[temino da materia: {}]".format(materia.nome)
                        else:
                            if verificador == True:
                                data.descricao += "[tem aula: {}]".format(materia.nome)
                            else:
                                pass
                    else:
                        if materia.inicio == verificador_dia:
                            data.descricao += "[inicio da materia: {}]".format(materia.nome)
                        else:
                            pass    
        for data in calendario:
            if data.dia == '---':
                pass
            else:
                for atividade in atividades:
                    if atividade.fim >= datetime.date(ano, mes, int(data.dia)):
                        if atividade.fim == datetime.date(ano, mes, int(data.dia)):
                            data.descricao += "[termino da atividade: {}]".format(atividade.nome)
                        else:
                            if atividade.intervalo == True:
                                data.descricao += "[lembrete da atividade: {}]".format(atividade.nome)
                            else:
                                pass
                    else:
                        if atividade.inicio == datetime.date(ano, mes, int(data.dia)):
                            data.descricao += "[inicio da atividade: {}]".format(atividade.nome)
                        else:
                            pass
        for data in calendario:
            if data.dia == '---':
                pass
            else:
                for evento in eventos:
                    if evento.fim >= datetime.date(ano, mes, int(data.dia)):
                        if evento.fim == datetime.date(ano, mes, int(data.dia)):
                            data.descricao += "[termino do evento: {}]".format(evento.nome)
                        else:
                            if evento.intervalo == True:
                                data.descricao += "[lembrete do evento: {}]".format(evento.nome)
                            else:
                                pass
                    else:
                        if evento.inicio == datetime.date(ano, mes, int(data.dia)):
                            data.descricao += "[inicio do evento: {}]".format(evento.nome) 
                        else:
                            pass
        for data in calendario:
            if data.dia == '---':
                pass
            else:
                for tarefa in tarefas:
                    if tarefa.fim >= datetime.date(ano, mes, int(data.dia)):
                        if tarefa.fim == datetime.date(ano, mes, int(data.dia)):
                            data.descricao += "[termino da tarefa: {}]".format(tarefa.nome)
                        else:
                            if tarefa.intervalo == True:
                                data.descricao += "[lembrete tarefa: {}]".format(tarefa.nome)
                            else:
                                pass
                    else:
                        if tarefa.fim == datetime.date(ano, mes, int(data.dia)):
                            data.descricao += "[inicio da tarefa: {}]".format(tarefa.nome)
                        else:
                            pass
    formata_saida(calendario)
    return calendario


def formata_saida(calendario):
    lista_atividades = []
    lista_evento = []
    lista_tarefa = []
    lista_materia = []
    mensagens = []
    for data in calendario:
        if data.dia == '---':
            pass
        else:
            strings = data.descricao.split(']')
            for string in strings:
                if "inicio da tarefa: " in string:
                    mensagens.append(string)
                else:
                    if "termino da tarefa: " in string:
                        mensagens.append(string)
                    else:
                        if "inicio do evento: " in string:
                            mensagens.append(string)
                        else:
                            if "termino do evento: " in string:
                                mensagens.append(string)
                            else:
                                if "inicio da atividade: " in string:
                                    mensagens.append(string)
                                else:
                                    if "termino da atividade: " in string:
                                        mensagens.append(string)
                                    else:
                                        if "inicio da materia: " in string:
                                            mensagens.append(string)
                                        else:
                                            if "temino da materia: " in string:
                                                mensagens.append(string)
                                            else: 
                                                if "lembrete tarefa: " in string:
                                                    string = string.split("[lembrete tarefa: ")
                                                    lista_tarefa.append(string)
                                                else:
                                                    if "lembrete do evento: " in string:
                                                        string = string.split("[lembrete do evento: ")
                                                        lista_evento.append(string)
                                                    else:
                                                        if "lembrete da atividade: " in string:
                                                            string = string.split("[lembrete da atividade: ")
                                                            lista_atividades.append(string)
                                                        else:
                                                            if "tem aula: " in string:
                                                                if 'temino da materia: ' in string:
                                                                    pass
                                                                else:
                                                                    string = string.split("[tem aula:")
                                                                    lista_materia.append(string)

            saida_materia = "você tem aula de: "                                                    
            for materia in lista_materia:
                saida_materia += materia
            saida_evento = "lembrete dos eventos"


def cria_mes(mes,ano):
    quantidade_dias = calendar.monthrange(ano, mes)[1]
    informacoes = []
    for i in range(1, quantidade_dias + 1):
            if i == 1:
                dia1 = datetime.date(ano,mes,i).weekday()
                if dia1 != 0:
                    while dia1 != 0:
                        informacoes.append(cl.calendario("---","---","---","---"))
                        dia1 -= 1
                dia = datetime.date(ano,mes,i).weekday()
                informacoes.append(cl.calendario(i,converte_dia(dia),"---"," "))
            else:
                dia = datetime.date(ano,mes,i).weekday()
                informacoes.append(cl.calendario(i,converte_dia(dia),"---"," "))
    while True:
        if len(informacoes) % 7 == 0:
            break
        else:
            informacoes.append(cl.calendario("---","---","---","---"))
    informacoes_completas = completa_descricao(2,2024,"italonunespereira@outlook.com",informacoes)
    if informacoes_completas == False:
        informacoes = informacoes_completas
    else:
        pass
    tamanho = len(informacoes)/7
    calendario  = [[] for _ in range(int(tamanho))]
    contador = 7
    i = 0
    for linha in calendario:
        while contador != 0:
            linha.append(informacoes[i])
            i+=1
            contador-=1
        contador = 7 
    return calendario


cria_mes(2, 2024)