from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from alchemyClasses.usuarios import usuarios

from model.model_rentar import ver_rentas, encontrar_renta, cambiar_fecha_renta, eliminar_renta, eliminar_todas_las_rentas
from model.model_peliculas import ver_peliculas, encontrar_pelicula, cambiar_nombre_peli_por_id, cambiar_nombre_peli_por_nombre, eliminar_pelicula, eliminar_todas_las_peliculas
from model.model_usuarios import ver_usuarios, encontrar_usuario, cambiar_nombre_usuario_por_id, cambiar_nombre_usuario_por_nombre, eliminar_usuario, eliminar_todos_los_usuarios

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        
        
        ver_rentas()