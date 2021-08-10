from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'tus_monedas' not in request.session:
        request.session['tus_monedas'] = 0
        request.session['salidapost'] = [{
            "msg": "",
            "color": "azul",
            "time": ""
        }]
    return render(request, 'index.html')

def process_money (request):
    selector = request.POST['monedas']
    #
    if selector == '0':
        request.session['tus_monedas'] = 0
        request.session['salidapost'] = [{
            "msg": "",
            "color": "azul",
            "time": ""
        }]
    #
    if selector == '1':
        obtenidas = randInt(10, 20)
        request.session['tus_monedas'] += obtenidas
        request.session['salidapost'].append(actividades(obtenidas))
    #
    if selector == '2':
        obtenidas = randInt(5, 10)
        request.session['tus_monedas'] += obtenidas
        request.session['salidapost'].append(actividades(obtenidas))
    #
    if selector == '3':
        obtenidas = randInt(2, 5)
        request.session['tus_monedas'] += obtenidas
        request.session['salidapost'].append(actividades(obtenidas))
    #
    if selector == '4':
        obtenidas = randInt(-50, 50)
        request.session['tus_monedas'] += obtenidas
        request.session['salidapost'].append(actividades(obtenidas))
    #
    return redirect("/")

def randInt(min, max):
    num = random.random() * (max-min) + min
    return round (num)

def actividades (valor):
    if valor >= 0:
        salida = {
        "msg": f"Ganáste {valor} monedas",
        "color": "azul",
        "time": strftime("%Y-%m-%d %H:%M:%S", gmtime())
        }

    if valor  < 0:
        salida = {
        "msg": f"Perdiste {valor} monedas",
        "color": "rojo",
        "time": strftime("%Y-%m-%d %H:%M:%S", gmtime())
        }
    return salida
