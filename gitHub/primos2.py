#proyecto euler reslizado exitosamente
#3 de agosto de 2014
#respuesta es el valor final de num = 6857
#los factores completos de num son 6857, 1471, 839, 71
#num2 es un valor intermedio de prueba

num = 600851475143
num2 = 10086647

def generador(upper):
	lista = xrange(5,upper,2)
	for item in lista:
		yield item


def primos(upper):
	inicio = [2,3]
	h = generador(upper)
	while True:
		try:
			k = h.next()
			control = True
			for item in inicio:
				if k%item == 0:
					control = False
					break
			if control:
				inicio.append(k)
		except:
			break
		
	return inicio

resp = []
tal = primos(1500)

for item in tal:
	while num%item == 0:
		num = num/item
		if num == 1: break
		resp.append(item)
resp.append(num)
