from flask import Flask, request, jsonify
from conexion import con_postgres
from . import routes

@routes.route("/variante", methods=["GET"])
def get_variante(id):
    """Obtener variante"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from variante where id = %s", (id,))
    variante = conexion.fetchall()   
    conexion.close()
    print(variante)
    return jsonify(variante)