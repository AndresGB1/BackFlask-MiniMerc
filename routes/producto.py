"""Utilizar flask y la conexión con postgresql para acceder a la base de datos de productos"""
from types import NoneType
from flask import jsonify
from conexion import con_postgres, con_redis
from flask_jwt_extended import jwt_required
from . import rutas
import ast

@rutas.route("/productos", methods=["GET"])
def get_productos():
    """Obtener todos los productos"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from producto")
    producto = conexion.fetchall()
    conexion.close()
    return jsonify(producto)

@rutas.route("/productos/<string:categoria>", methods=["GET"])
def get_productos_categoria(categoria):
    """Obtener todos los productos por categoria
        obtenerlos de Redis y en caso que no exista
        Guardarlos en Redis y expirar en 10 minutos
       "select p.* from condicion as c, producto as p where c.id_categoria = '{0}' and c.id_producto = p.id_producto".format(categoria)
    """
    con = con_redis.redis
    conexion = con.get(categoria)
    if conexion is None:
        con = con_postgres.postgres
        conexion = con.cursor()
        conexion.execute("select p.* from condicion as c, producto as p where c.id_categoria = '{0}' and c.id_producto = p.id_producto".format(categoria))
        producto = conexion.fetchall()
        conexion.close()
        con = con_redis.redis
        con.set(categoria, str(producto), ex=600)
        print("Retornando de la base de datos")
        return jsonify(producto)
    else:
        print("Retornando de Redis")
        return jsonify(ast.literal_eval(conexion.decode("utf-8")))
    
@rutas.route("/producto/<string:id>", methods=["GET"])
def get_producto(id):
    """Obtener producto por id"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from producto where id_producto = {0}".format(id))
    producto = conexion.fetchall()
    conexion.close()
    return jsonify(producto)



