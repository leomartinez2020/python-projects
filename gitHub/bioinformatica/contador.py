# -*- coding: utf-8 -*-
"""El codigo corresponde al ejercicio de bioinformatica
   Bioinformatica Coursera octubre 27 de 2014
   'Solve the frequent words problem'
    Input: A string Text and an integer k.
     Output: All most frequent k-mers in Text.

    Sample Input:
         ACGTTGCATGTCGCATGATGCATGAGAGCT
         4

    Sample Output:
         CATG GCAT
"""

class Kmeros(object):
    def __init__(self, ruta):
        self.ruta = ruta
        
    def lector_arch(self):
        """El archivo de texto es como se muestra arriba (sample input)
            ejemplo: secuencia.txt
            la segunda linea debe ser un numero asi que mas tarde se convierte
            a int
        """
        with open(self.ruta,'r') as arch:
            texto = arch.readline()
            valor = arch.readline()
        return texto, valor

    def contador(self, cadena, piece):
        indice, cont, c = 0,0,0 
        while indice != -1:
            indice = cadena.find(piece, c)
            if indice != -1:
                cont += 1
            c = indice + 1
        return cont

    def iterando(self, cadena, num):
        """

        """
        for i in range(0,len(cadena) - num + 1):
            pedazo = cadena[i:i+num]
            yield pedazo

    def contador2(self):
        ditto = dict()
        maximo = 0
        cadena, tamanio = self.lector_arch()
        peaso = self.iterando(cadena, int(tamanio))
        while True:
            try:
                p = peaso.next()
                if p not in ditto:
                    c = self.contador(cadena,p)
                    ditto[p] = c
                    if c > maximo:
                        maximo = c
            except StopIteration:
                break
        sec = []
        for item in ditto:
            if ditto[item] == maximo:
                sec.append(item)
        return ' '.join(sec)
