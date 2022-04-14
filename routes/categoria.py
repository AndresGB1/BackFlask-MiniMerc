from flask import jsonify
from conexion import con_postgres
from . import rutas

@rutas.route("/categorias", methods=["GET"])
def get_categorias():
    """Obtener todas las categorias"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from categoria")
    categoria = conexion.fetchall()
    conexion.close()
    return jsonify(categoria)