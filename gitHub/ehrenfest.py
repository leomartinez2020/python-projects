import random
#Ehrenfest
#tablero
def tablero():
    a = []
    for i in range(4):
        b = ['O']*8
        a.append(b)
        c =['X']*8
        a.append(c)
    return a

def escoge():
    x = random.randint(0,7)
    y = random.randint(0,7)
    return (x,y)

def remplaza(tablero):
    x, y = escoge()
    if tablero[x][y] == 'O':
        tablero[x][y] = 'X'
    else:
        tablero[x][y] = 'O'
    

def visualiza(tablero):
    equis, redondo = 0, 0
    for row in tablero:
        equis += row.count('X')
        redondo += row.count('O')
        print ' '.join(row)
    print 'X: %d' %equis, 'O: %d' %redondo

def doblar(tablero):
    x, y = escoge()
    if tablero[x][y] == 'O':
        while True:
            w, z = escoge()
            if w != x and z != y:
                if tablero[w][z] == 'X':
                    tablero[w][z] = 'O'
                    break
    else:
        while True:
            w, z = escoge()
            if w != x and z != y:
                if tablero[w][z] == 'O':
                    tablero[w][z] = 'X'
                    break
