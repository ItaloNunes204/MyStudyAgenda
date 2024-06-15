import classes as cl
import banco as bd
import datetime
import calendar
import formatador as fr


# converte valores inteiros em strings dos dias  
def converte_dia(dia):
    #converte o dia em numeros em palavras 
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
                            return "Domingo"


# coleta as informações das materias 
def coleta_informacao_materia(email, dia):
    materias = bd.get_all_materia(email) # coleta todas as materias
    if materias != False or materias != 'sem registros': # verifica se tinha registro ou ocorreu algum erro 
        materias_validas = [] # lista de materia
        for materia in materias: # loop de materias
            if dia <= materia.fim: # verifica se o termino da materia esta antes do fim da materia 
                materias_validas.append(materia)
        return materias_validas # retorna a lista 
    else: # caso contrario
        return False


# coleta as informações das atividades 
def coleta_informacao_atividades(email, dia_validacao):
    atividades = bd.get_all_atividades(email) # coleta todas as atividades 
    if atividades != False or atividades != "sem registros": # verifica se tinha registros ou correu algum erro
        atividades_validas = [] # lista de atividades 
        for atividade in atividades: # loop de atividades 
            if dia_validacao <= atividade.fim: # verifica se o termino da atividade esta antes do fim da atividade 
                atividades_validas.append(atividade)
        return atividades_validas # retorna a lista 
    else: # caso contrario 
        return False


# coleta as informações dos eventos 
def coleta_informacao_eventos(email, dia_validacao):
    eventos = bd.get_all_eventos(email) # coleta todos os eventos 
    if eventos == False or eventos == 'sem registros': # verifica se existe registros ou ocorreu algum tipo de erro 
        return False
    else:
        eventos_validos = [] # lista de eventos 
        for evento in eventos: # loop de eventos 
            if dia_validacao <= evento.fim: # verifica se o dia esta entre o fim do evento 
                eventos_validos.append(evento)
        return eventos_validos # retorna a lista 


# coleta as informações das atividades
def coleta_informacao_tarefas(email, dia_validacao):
    tarefas = bd.get_all_tarefas(email) # coleta todas as tarefas 
    if tarefas != False or tarefas != "sem registros": # verifica se existe registro ou ocorreu algum tipo de erro
        tarefas_validas = [] # lista de tarefa
        for tarefa in tarefas: # loop de tarefas
            if dia_validacao <= tarefa.fim: # verifica se o dia esta antes do termino da tarefa 
                tarefas_validas.append(tarefa) 
        return tarefas_validas # retorna a lista de tarefas
    else:
        return False


# formata as informações das classes 
def formata_saida(calendario):
    lista_atividades = [] # lista de atividades 
    lista_evento = [] # lista de eventos 
    lista_tarefa = [] # lista de tarefas 
    lista_materia = [] # lista de materias
    mensagens = []

    for dia in calendario:
        if dia.dia == "---":# verifica se a classe é nula 
            pass
        else: # caso não for nula 
            strings = data.descricao.split(']')#  quebra a string 
            for string in strings:#loop da lista de strings
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
                                                                string = string.split("[tem aula: ")
                                                                lista_materia.append(string)
                                                            else:
                                                                pass

            saida_materia = " você tem aula: "
            for materia in lista_materia:
                saida_materia += materia 
                saida_materia += " "

            saida_evento = " lembrete de eventos: "
            for evento in lista_evento:
                saida_evento += evento
                saida_evento += " "                           

            saida_atividade = " lembrete de atividade: "
            for atividade in lista_atividades:
                saida_atividade += atividade
                saida_atividade += " "
            
            saida_tarefa = " lembrete de tarefa: "
            for tarefa in lista_tarefa:
                saida_tarefa += tarefa
                saida_tarefa += " "
            saida_final = mensagens + " " +saida_materia+" "+saida_evento+" "+saida_atividade+" "+saida_tarefa
            dia.descricao = saida_final
    return calendario


# completa as classes com as informações 
def completa_descricao(mes, ano, email, calendario):
    # cria um objeto do tipo date 
    dia = datetime.date(ano, mes, 1)
    # coleta as informações e armazena em vetores 
    materias = coleta_informacao_materias(email, dia)
    # coleta as informações e armazena em vetores 
    atividades = coleta_informacao_atividades(email, dia)
    # coleta as informações e armazena em vetores 
    eventos = coleta_informacao_eventos(email, dia)
    # coleta as informações e armazena em vetores 
    tarefas = coleta_informacao_tarefas(email, dia)
    # verifica se as informações estão com algum tipo de erro
    if materias == False or atividades == False or eventos == False or tarefas == False:
        return False
    else:
        for dia in calendario: # loop dos dias
            if dia.dia == "---": # verifica se a classe é nula 
                pass
            else: # caso a classe não for nula 
                # cria um objeto do tipo date 
                verificador_dia = datetime.date(ano, mes, int(dia.dia))
                for materia in materias: # loop das matérias
                    if materia.fim >= verificador_dia and materia.inicio < verificador_dia: # verifica sse o dia atual esta entre o intervalo da materia 
                        dias_materias = fr.formata_dias_saida(materia.dias) # coleta as informações da materia formatada 
                        dias_materias = dias_materias.split(',') # transforma as informações em um vetor 
                        verificador = False # cria um verificador para a validação dos dia
                        # loop para verificar se a materia esta prevista em determinado dia da semana
                        for dia_materia in dias_materias:
                            if dia_materia.lower() == dia.diaS.lower():
                                verificador = True
                                break
                        if materia.fim == verificador_dia: # verifica se o atual dia e o mesmo dia do temino da materia
                            # se no dia atual tiver previsto aula
                            if verificador == True:
                                dia.descricao += "[temino da materia: {}]".format(materia.nome)
                                dia.descricao += "[tem aula: {}]".format(materia.nome)
                            else: # se no dia atual não tiver previsto aula
                                dia.descricao += "[temino da materia: {}]".format(materia.nome)
                        else: # caso o dia atual esteja entre o inicio e fim da materia
                            if verificador == True:
                                dia.descricao += "[tem aula: {}]".format(materia.nome)
                            else:
                                pass
                    else: # caso o dia atual não esteja entre o termino da materia
                        if materia.inicio == verificador_dia: # verifica se o nicio da materia é o mesmo do dia atual 
                            dia.descricao += "[inicio da materia: {}]".format(materia.nome)
                        else:
                            pass

                for atividade in atividades: # loop das atividades
                    if atividade.fim >= verificador_dia and atividade.inicio < verificador_dia: # verifica se o dia atual esta entre o intervalo da atividade 
                        if atividade.fim == verificador_dia: # verifica se o termino da atividade é o dia atual 
                            dia.descricao += "[termino da atividade: {}]".format(atividade.nome)
                        else: # caso não for o termino da atividade 
                            if atividade.intervalo == True: # verifica se é para criar um lembrete
                                dia.descricao += "[lembrete da atividade: {}]".format(atividade.nome)
                            else: # caso não for para criar um lembrete
                                pass
                    else: # caso o dia atual 
                        if atividade.inicio == verificador_dia:
                            dia.descricao += "[inicio da atividade: {}]".format(atividade.nome)
                        else:
                            pass

                for evento in eventos: # loop dos eventos 
                    if evento.fim >= verificador_dia and evento.inicio < verificador_dia: # verifica se o dia atual esta entre o intervalo do evento 
                        if evento.fim == verificador_dia: # verifica se o dia atual é o mesmo dia do termino do evento
                            dia.descricao += "[termino do evento: {}]".format(evento.nome)
                        else: # caso contrario 
                            if evento.intervalo == True: # verifica se é pra criar um lembrete para o evento
                                dia.descricao += "[evento: {}]".format(evento.nome)
                            else: # caso contrario
                                pass
                    else: # caso o dia atual não esteja entre o intervalo dos eventos 
                        if evento.inicio == verificador_dia: # verifica se o dia atual é o inicio do evento
                            dia.descricao += "[inicio do evento: {}]".format(evento.nome) 
                        else: # caso contrario
                            pass

                for tarefa in tarefas: # loop das tarefas
                    if tarefa.fim >= verificador_dia and tarefa.inicio < verificador_dia: # verifica se o dia atual esta entre o intervalo da tarefa
                        if tarefa.fim == verificador_dia: # verifica se o dia atual é o mesmo dia do termino da atividade 
                            dia.descricao += "[termino da tarefa: {}]".format(tarefa.nome)
                        else: # caso contrario
                            if tarefa.intervalo == True: # verifica se é para criar um lembrete para a tarefa
                                dia.descricao += "[lembrete tarefa: {}]".format(tarefa.nome)
                            else: # caso contrario
                                pass
                    else: # caso o dia atual não estiver entre o intervalo da tarefa
                        if tarefa.inicio == verificador_dia: # verifica se o inicio da tarefa é o dia atual 
                            dia.descricao += "[inicio da tarefa: {}]".format(tarefa.nome)
                        else: # caso contrario 
                            pass
        
        calendario = formata_saida(calendario)
        return calendario


# cria uma lista de listas com as classes de dias 
def cria_mes(mes, ano, email):
    quantidade_dias = calendar.monthrange(ano, mes)[1] # quantidade de dias do mes
    informacoes = [] # vetor que armazena as classes do calendario 
    # loop que completa o vetor com as classe
    for i in range(1, quantidade_dias + 1):
        # verifica se e o dia primeiro
        if i == 1: # se for dia 1
            # cria um objeto do tipo datetime e coleta o dia da semana
            dia1 = datetime.date(ano, mes, i).weekday()
            if dia1 != 0: # se o dia não for segunda-feira completa com uma classe nula 
                while dia1 != 0:
                    informacoes.append(cl.calendario("---", "---", "---", "---"))
                    dia1 -= 1
            # apos completar o vetor com as classes nulas vamos completar com as classes corretas 
            dia_semana = datetime.date(ano, mes, i).weekday()
            informacoes.append(cl.calendario(i, converte_dia(dia_semana), "---", "---"))
        else: # caso não for o dia 1
            dia_semana = datetime.date(ano,mes,i).weekday() #  coleta o dia da semana
            informacoes.append(cl.calendario(i, converte_dia(dia_semana), "---", "---")) # completa o vetor com as classes dos dias
    # verifica se o vetor esta com o tamanho coreto 
    while True:
        # verifica se o vetor esta com todas as semanas completas  
        if len(informacoes) % 7 == 0:
            break
        else: # caso não esteja com as semanas completas a semana e completada com uma classe nula 
            informacoes.append(cl.calendario("---", "---", "---", "---"))
    # completa as informações da lista         
    informacoes_completas = completa_descricao(mes, ano, email, informacoes)        
    if informacoes_completas != False: # verifica se ocorreu algum erro
        # atualiza a lista de informaçoes com o novo vetor com as informações completas
        informacoes = informacoes_completas
    else: # caso ocorra algum erro vai ser retornado apenas a lista as classes incompletas 
        pass

    quantidade_semanas = len(informacoes)/7 # coleta a quantidade de semanas
    calendario = [[] for _ in range(int(quantidade_semanas))] # cria uma lista de semanas em que cada semana tem 7 classes 
    contador = 7 # contador para completar a lista de dias 
    i = 0 # contador para completar a lista de dias 
    for semana in calendario: # loop para completar as informações 
        while contador != 0: # verifica se a semana não esta completa 
            # completa a semana com as classes da lista de informações 
            semana.append(informacoes[i])
            i+=1
            contador -= 1
        contador = 7
    # retorna a lista de semanas 
    return calendario
