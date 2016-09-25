#generador de numeros primos 
#09 de agosto de 2014

def primos():
    """invocando next() genera un primo a la vez"""
    d = [2]
    x = 1
    while True:
        yield d[-1]
        while True:
            control = True
            x += 2
            for item in d:
                if x%item == 0:
                    control = False
                    break
            if control:
                d.append(x)
                break

#project euler problem 3 solution
num = 600851475143
valor = 600851475143
resp = []
p = primos()
while num > valor**0.5:
	nprimo = p.next()
	if num%nprimo == 0:
		print "encontre uno!"
		num = num/nprimo
		resp.append(nprimo)

resp.append(num)
print "la respuesta al problema 3 es %d" %num
