class Conta:
    def __init__(self, nome, senha, curso, periodo, universidade, interna, externa, creditos, email):
        self.nome = nome
        self.senha = senha
        self.curso = curso
        self.periodo = periodo
        self.universidade = universidade
        self.notificacaoInterna = interna
        self.notificacaoExterna = externa
        self.nCreditos = creditos
        self.email = email


class Materia:
    def __init__(self, nome, inicio, fim, creditos, nota, observacao, dias, horario, email, estado, id_materia):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.creditos = creditos
        self.nota = nota
        self.observacao = observacao
        self.dias = dias
        self.horario = horario
        self.email = email
        self.estado = estado
        self.idMateria = id_materia


class Atividade:
    def __init__(self, nome, nota, nota_atividade, intervalo, inicio, fim, horario, estado, observacao, email,
                 nome_materia, id_materia, id_atividade):
        self.nome = nome
        self.nota = nota
        self.notaAtividade = nota_atividade
        self.intervalo = intervalo
        self.inicio = inicio
        self.fim = fim
        self.horario = horario
        self.estado = estado
        self.observacao = observacao
        self.email = email
        self.nomeMateria = nome_materia
        self.idMateria = id_materia
        self.idAtividade = id_atividade


class Evento:
    def __init__(self, nome, inicio, fim, intervalo, observacao, estado, horario, lugar, email, id_evento):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.intervalo = intervalo
        self.observacao = observacao
        self.estado = estado
        self.horario = horario
        self.lugar = lugar
        self.email = email
        self.idEvento = id_evento


class Tarefa:
    def __init__(self, nome, inicio, fim, intervalo, horario, lugar, estado, observacao, tipo, email, id_tarefa):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.intervalo = intervalo
        self.horario = horario
        self.lugar = lugar
        self.estado = estado
        self.observacao = observacao
        self.tipo = tipo
        self.email = email
        self.idTarefa = id_tarefa


class calendario:
    def __init__(self, dia, diaS ,tipo, descricao):
        self.dia = dia
        self.diaS = diaS
        self.tipo = tipo
        self.descricao = descricao
