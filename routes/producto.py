"""Utilizar flask y la conexión con postgresql para acceder a la base de datos de productos"""
from flask import jsonify
from conexion import con_postgres

from . import rutas

@rutas.route("/productos", methods=["GET"])
def get_productos():
    """Obtener todos los productos"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from producto")
    producto = conexion.fetchall()
    conexion.close()
    print(producto)
    return jsonify(producto)

@rutas.route("/producto/<string:id>", methods=["GET"])
def get_producto(id):
    """Obtener producto por id"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from producto where id_producto = {0}".format(id))
    producto = conexion.fetchall()
    conexion.close()
    print(producto)
    return jsonify(producto)