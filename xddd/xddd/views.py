from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import Template,Context
from datetime import *
from django.template import loader

def probando_template(self):
    dia_de_hoy = datetime.now()
    nombre = "luca"
    apellido = "veintemilla"
    notas = [1,4,2,6,7,4,2,8,5]
    edad = 19
    dicc = {"nombre":nombre,"apellido":apellido,"edad":edad,"dia":dia_de_hoy,"notas":notas}

# mihtml = open("C:/Users/lukia/OneDrive/Documentos/biblioteca/programacion/Python/coder python/django pruebas/proyectoprueba/templates/template.html")

# plantilla = Template(mihtml.read())

# mihtml.close()

# micontexto = Context(dicc)

    plantilla = loader.get_template("template.html")


    documento = plantilla.render(dicc)
        
    return HttpResponse(documento)

def prueba_loader_otra_plantilla(self,nombre):
    dia = datetime.now()
    dicc = {"nombre":nombre,"diahoy":dia}

    plantilla = loader.get_template("prueba.html")
    
    doc = plantilla.render(dicc)
    return HttpResponse(doc)


def nombre(self,nombre):
    doc = f"mi nombre es : <br> {nombre}"

    return HttpResponse(doc)


def sumar(self,num):
    num = int(num)
    result =  num+num
    
    return HttpResponse(f"el resultado de la suma fue: {result}")


def diahoy(self):
    hoy = datetime.date()
    return HttpResponse(hoy)