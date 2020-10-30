from flask import Flask, render_template
from datetime import date
from random import choice

app = Flask(__name__)

reglas = {
    'piedra': {
        'piedra':   {'resultado': 0,  'mensaje': 'Empate'},
        'papel':    {'resultado': -1, 'mensaje': 'Papel envuelve piedra'},
        'tijeras':  {'resultado': 1,  'mensaje': 'Piedra aplasta tijeras'},
        'lagarto':  {'resultado': 1,  'mensaje': 'Piedra aplasta lagarto'},
        'spock':    {'resultado': -1, 'mensaje': 'Spock vaporiza piedra'}

    },
    'papel': {
        'piedra':   {'resultado': 1,  'mensaje': 'Papel envuelve piedra'},
        'papel':    {'resultado': 0,  'mensaje': 'Empate'},
        'tijeras':  {'resultado': -1, 'mensaje': 'Tijeras cortan papel'},
        'spock':    {'resultado': 1,  'mensaje': 'Papel desautoriza a spock'},
        'lagarto':  {'resultado': -1, 'mensaje': 'Lagarto devora papel'}
    },
    'tijeras': {
        'piedra':   {'resultado': -1, 'mensaje': 'Piedra aplasta tijeras'},
        'papel':    {'resultado': 1,  'mensaje': 'Tijeras cortan papel'},
        'tijeras':  {'resultado': 0,  'mensaje': 'Empate'},
        'lagarto':  {'resultado': 1,  'mensaje': 'Tijeras decapitan lagarto'},
        'spock':    {'resultado': -1, 'mensaje': 'Spock rompe tijeras'}
    },
    'lagarto':{
        'piedra':   {'resultado': 1,  'mensaje': 'Lagarto devora papel'},
        'papel':    {'resultado': 1,  'mensaje': 'Lagarto devora papel'},
        'tijeras':  {'resultado': -1, 'mensaje': 'Tijeras decapitan lagarto'},
        'lagarto':  {'resultado': 0,  'mensaje': 'Empate'},
        'spock':    {'resultado': -1, 'mensaje': 'Lagarto envenena a spock'}
    },
    'spock': {
        'piedra':   {'resultado': 1,  'mensaje': 'Spock vaporiza piedra'},
        'papel':    {'resultado': -1, 'mensaje': 'Papel desautoriza a spock'},
        'tijeras':  {'resultado': 1,  'mensaje': 'Spock rompe tijeras'},
        'spock':    {'resultado': 0,  'mensaje': 'Empate'},
        'lagarto':  {'resultado': -1, 'mensaje': 'Lagarto envenena a spock'}
    },
}

objetos = list(reglas.keys())

@app.route('/')
def inicio():
    f = date.today()
    return render_template(
        'selecciona_tiro.html',
        Fecha=f)

@app.route('/tiro/<tiro_jugador>')
def tiro(tiro_jugador):
    tiro_sheldon = choice(objetos)
    resultado = reglas[tiro_jugador][tiro_sheldon]['resultado']
    mensaje = reglas[tiro_jugador][tiro_sheldon]['mensaje']
    return render_template(
        'despliega resultado.html',
        tiro_jugador = tiro_jugador,
        tiro_sheldon = tiro_sheldon,
        resultado = resultado,
        mensaje = mensaje)