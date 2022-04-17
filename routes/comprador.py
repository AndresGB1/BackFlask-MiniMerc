from flask import jsonify
from conexion import con_postgres
from . import rutas

@rutas.route("/comprador/<string:id>", methods=["GET"])
def get_comprador(id):
    """Obtener comprador"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from comprador where id_comprador = {0}".format(id))
    comprador = conexion.fetchall()   
    conexion.close()
    return jsonify(comprador)