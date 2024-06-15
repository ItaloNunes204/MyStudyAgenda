import banco as bd
import classes as cl
import formatador as fr
import datetime

email = "italonunespereira@outlook.com"
data_inicio = datetime.date(2024,2,1)
data_fim = datetime.date(2024,3,2)
nome_materia = "calculo"
hora = datetime.datetime.strptime("14:30", '%H:%M')

#------------ cadastro materia -------------

for i in range(100):
    evento = cl.Evento("evento" + str(i),data_inicio,data_fim,True,'GGGG',True,hora,'SALA',email,None)
    print(bd.cria_evento(evento))

print("tarefas")
for i in range(100):
    tarefa = cl.Tarefa("tarefa"+str(i),data_inicio,data_fim,True,hora,'sala',True,'hhh','sasa',email,None)
    print(bd.cria_tarefa(tarefa))