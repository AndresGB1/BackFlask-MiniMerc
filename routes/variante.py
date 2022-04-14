from flask import  jsonify
from conexion import con_postgres
from . import rutas

@rutas.route("/variante/<string:id>", methods=["GET"])
def get_variante(id):
    """Obtener variante"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from variante where id_variante = {0}".format(id))
    variante = conexion.fetchall()   
    conexion.close()
    return jsonify(variante)

    
@rutas.route("/producto/<string:id>/variantes", methods=["GET"])
def get_variante_producto(id):
    """Obtener variante"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from variante where producto = {0}".format(id))
    variantes = conexion.fetchall()   
    conexion.close()
    return jsonify(variantes)
