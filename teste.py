import banco as bd
import classes as cl

email = "italonunespereiraaa@outlook.com"
id = 0


conta = cl.Conta('italo','senddasha','esafasca','1','ufmg',True,True,0,email)
materia = cl.Materia("tefsdfsdste","2023/05/22","2023/05/22",35,0,"ssadsadv",'dddsrrd',"14.55",email,True,17)
trefa = cl.Tarefa("ffsssf","2023/05/22","2023/05/22",True,'15:55',"casa",True,'rrr','rrrr',email,14)
evento = cl.Evento('saaaafas',"2023/05/22","2023/05/22",True,'kcada',True,'14:55','rrr',email,15)
atividade = cl.Atividade('AafasfFA',0,0,True,"2023/05/22","2023/05/22",'14:55',True,'rrrrr',email,'TESTE',17,13)
atividade1 = cl.Atividade('000',0,0,False,"2023/05/22","2023/05/22",'14:55',True,'ddd',email,'da',17,13)


#print(bd.cria_conta(conta))
#print(bd.cria_materia(materia))
#print(bd.cria_tarefa(trefa))
#print(bd.cria_evento(evento))
#print(bd.cria_atividade(atividade))


#print(bd.modifica_conta(conta))
#print(bd.modifica_materia(materia))
#print(bd.modifica_tarefa(trefa))
#print(bd.modifica_evento(evento))
#print(bd.modifica_atividade(atividade))


#print(bd.get_conta(email))
#print(bd.get_materia(email,True))
#print(bd.get_materiaID(email,17))
#print(bd.get_tarefas(email,True))
#print(bd.get_tarefasID(email,14))
#print(bd.get_evento(email,True))
#print(bd.get_eventoID(email,15))
#print(bd.get_atividade(email,True))
#print(bd.get_atividadeID(email,13))

