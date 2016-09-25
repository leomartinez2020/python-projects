import os
import sys

base_url = "https://github.com/leonardo384/"

repo = sys.argv[1]  # el nombre del repository

arch = base_url + repo + ".git"

def clonar():
    """
    clona el git repo pasado como argumento
    """
    resp = "git clone " + arch 
    os.system(resp)
    print('clonado')

def borrar_git():
    """
    elimina el archivo .git innecesario
    """
    remover = "rm -rf " + repo + "/.git"
    os.system(remover)

def agregar_y_comprometer():
    """
    ejecuta git add y git commit con mensaje
    """
    os.system('git add .')
    msg = "Add {} folder".format(repo)
    res = "git commit -m \"{}\"".format(msg)
    os.system(res)

def empujar():
    msg = "git push -u origin master"
    os.system(msg)

if __name__ == "__main__":
    clonar()
    borrar_git()
    agregar_y_comprometer()
    empujar()
