#!/usr/bin/python
# -*- coding: utf-8 -*-

#programa creado el 05 de diciembre
#busca empleos en los clasificados de El heraldo
#Ejemplo de output:
#Inmobiliarios experiencia en ventas manejo de sistemas, excelente presentacion
#personal y fluidez verbal fecha: 25/11/2014
#Cargos Varios, Administrador, exper:2 años, Vendedor institucional para
#empresa de bebidas. Zona Bqlla y PtoColombia. Basico+comisiones.
#fecha: 25/11/2014

import requests

pagina = "2"
heraldo = "http://empleosh.co/frontend.empleos.php/avisos/oferta/oferta-laboral?page=%s" %pagina
r = requests.get(heraldo,stream=True)
res = []
for line in r.iter_lines():
    if line:
        h = line.find("subtitle")
        if h != -1:
            k = line.find('</p>', h + 10)
            texto = line[h+10:k]  
        f = line.find("Publicado")
        if f != -1:
            texto2 = line[f+20:f+30]
            text = texto + " fecha: " + texto2
            text = text.decode('utf8')
            res.append(text)

for item in res:
    print(item)
    print()
