from flask import jsonify, request
from conexion import con_postgres
from . import rutas


@rutas.route("/tarjeta", methods=["POST"])
def post_tarjeta():
    con = con_postgres.postgres
    conexion = con.cursor()
    tipo = request.json.get("tipo", None)
    nombre = request.json.get("nombre", None)
    fecha = request.json.get("fecha", None)
    cvv = request.json.get("cvv", None)
    conexion.execute("insert into tarjeta (tipo, nombre, fecha, cvv) values ({0}, '{1}', '{2}', {3})".format(tipo, nombre, fecha, cvv))    
    con.commit()
    conexion.close()
    return jsonify({"status": "ok"})
