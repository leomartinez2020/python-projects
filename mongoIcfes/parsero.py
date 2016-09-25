#!/usr/bin/env python
# -*- coding: utf-8 -*-

prueba = "C:/Users/Camilo/Documents/AApython/PuntajesSABER2013.csv"#el archivo csv que vamos a procesar

from pymongo import MongoClient
import csv

def parsear(archivo, inicio):
    """
    abre un archivo csv y lo convierte en un generador desde
    el indice indicado (inicio)
    """
    c = 0
    with open(archivo) as f:
        reader = csv.reader(f, delimiter=';')#el csv de excel viene con punto y coma 
        for row in reader:
            if c == inicio:
                yield row
                break
            c += 1
        for row in reader:
            yield row

connection = MongoClient('localhost', 27017)#nos conectamos con el servidor de mongo

db = connection.saber#la base de datos se llama saber

coleccion = db.sabericfes#la coleccion se llama sabericfes

k = parsear(prueba, 3)

sec = k.next()
for i in range(len(sec)):#convertimos las claves a minuscula
    sec[i] = sec[i].lower()#para mayor comodidad
    
#la codificacion cp1252 es para convertir el texto en unicode
#tambien se puede usar iso-8859-1
#de otra forma mongo rechaza los datos
    
ditto = {}#creamos el diccionario (documento para mongo)

while True:
    for a, b in zip(sec,k.next()):
        if len(b) == 0:
            b = None
        elif b[0].isdigit():
            b = b.replace(',','.')#eliminamos la coma que viene de excel
            b = float(b)#convertimos texto a numero flotante
        else:
            b = b.decode('cp1252')#mongo requiere unicode
        ditto[a] = b
    coleccion.insert(ditto)#insetamos el diccionario (documento) en la base de datos
    ditto = {}#vaciamos el diccionario para seguir el ciclo
