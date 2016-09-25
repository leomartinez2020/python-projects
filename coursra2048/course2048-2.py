#segundo intento de 2048
#14 de junio de 2014


def quitaceros(secu):
        """
        elimina los ceros de una lista
        ejemplo: [2,0,0,2]  ->  [2,2]
        """
        helpo = []
        for item in secu:
                if item != 0:
                        helpo.append(item)
        return helpo


sec = [2,2,0,2,2,0,0,16,0,16]
print sec
helper = quitaceros(sec)
print helper

for i in range(len(helper)-1):   #aqui sumamos si los numeros
        if helper[i] == helper[i+1]:   # consecutivos son iguales
                helper[i] += helper[i+1]
                helper[i+1] = 0
                
def agregaceros(original,copia):
        """
        agrega ceros al final de una lista hasta completar
        la longitud original: [4] ->  [4,0,0,0]
        """
        copia = copia + [0]*(len(original)-len(copia))
        return copia

helper = quitaceros(helper)
print helper

helper = agregaceros(sec, helper)
print helper
