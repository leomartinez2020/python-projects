
#Primer intento de 2048
# 14 de junio de 2014
sec = [2,0,2,2]
helper = [0]*len(sec)
for i in range(len(sec)):
	if sec[i] != 0:
		helper[i] = sec[i]

k = helper.index(0)

if helper[k-1] == helper[k+1]:
		helper[k-1] += helper[k+1]
		helper = helper[:k] + helper[k+2:]


print helper
