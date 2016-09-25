import csv

resp = []
with open("C:/Users/Camilo/Dropbox/practicasMayo2014/level4-5.csv") as ficha:
	datos = csv.reader(ficha, delimiter=',')
	for row in datos:
		row = list(row)
		resp.append(row)

preguntas = resp[0][2:]
clue = resp[1][2:]

key = [False]*len(clue)

def califica(orden):
    """El orden del estudiante en la hoja de calculo"""
    orden -= 1
    student = resp[orden][2:]
    cont1 = 0
    cont2 = 0
    for x,y in zip(clue,student):
        if x == y and x != '':
            cont1 += 1
            key[cont2] = True
        cont2 += 1
    print key    
    print "Informe para %s" %resp[orden][1]
    print "Respuestas correctas: %d" %key.count(True)
    for item,valor,opcion,buena in zip(preguntas,key,student,clue):
        if valor:
            print item, "(", opcion, ")", "Correcto!"
        else:
            if item != '':
                print item, "(", opcion, ")", "Incorrecto"
                print "La respuesta era: %s" %buena
        
            
            
