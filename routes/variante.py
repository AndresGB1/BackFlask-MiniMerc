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
    print(variante)
    return jsonify(variante)

@rutas.route("/variante", methods=["GET"])
def get_variantes():
    """Obtener todas las variantes"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from variante")
    variante = conexion.fetchall()   
    conexion.close()
    print(variante)
    return jsonify(variante)
    

