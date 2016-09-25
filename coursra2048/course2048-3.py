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

def agregaceros(original,copia):
        """
        agrega ceros al final de una lista hasta completar
        la longitud original: [4] ->  [4,0,0,0]
        """
        copia = copia + [0]*(len(original)-len(copia))
        return copia

def merge(line):
    helper = quitaceros(line)
    for i in range(len(helper)-1):
        if helper[i] == helper[i+1]:
            helper[i] += helper[i+1]
            helper[i+1] = 0
    helper = agregaceros(line, quitaceros(helper))
    return helper
    
