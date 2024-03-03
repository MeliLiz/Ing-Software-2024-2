from flask import Blueprint, request, render_template, flash, url_for
from model import model_peliculas as mp

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')


"""@pelicula_blueprint.route('/')
def seccion_alumnos():
    return render_template('peliculas.html')"""