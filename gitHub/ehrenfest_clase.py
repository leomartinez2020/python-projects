import random
#Ehrenfest
#tablero
class Ehrenfest(object):
    def __init__(self):
        self.val_x = []
        self.val_o = []
        self.tablero = self.crear_tablero()
        
    def crear_tablero(self):
        a = []
        for i in range(4):
            b = ['O']*8
            a.append(b)
            c =['X']*8
            a.append(c)
        return a

    def escoge(self):
        x = random.randint(0,7)
        y = random.randint(0,7)
        return (x,y)

    def remplaza(self):
        x, y = self.escoge()
        if self.tablero[x][y] == 'O':
            self.tablero[x][y] = 'X'
        else:
            self.tablero[x][y] = 'O'
        self.valoresgraf()
        
    def valoresgraf(self):
        x, rondo = 0, 0
        for row in self.tablero:
            x += row.count('X')
            rondo += row.count('O')
        self.val_x.append(x)
        self.val_o.append(rondo)

    def visualiza(self):
        print
        equis, redondo = 0, 0
        for row in self.tablero:
            equis += row.count('X')
            redondo += row.count('O')
            print ' '.join(row)
        print
        print 'X: %d' %equis, '  O: %d' %redondo

    def doblar(self):
        x, y = self.escoge()
        if self.tablero[x][y] == 'O':
            while True:
                w, z = self.escoge()
                if w != x and z != y:
                    if self.tablero[w][z] == 'X':
                        self.tablero[w][z] = 'O'
                        break
        else:
            while True:
                w, z = self.escoge()
                if w != x and z != y:
                    if self.tablero[w][z] == 'O':
                        self.tablero[w][z] = 'X'
                        break
