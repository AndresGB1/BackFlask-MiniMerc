"""conexion con postgresql para acceder a la base de datos de carro de compras"""
from flask import jsonify, request
from conexion import con_postgres, con_redis
from . import rutas
from flask_jwt_extended import jwt_required
import ast
import datetime

@rutas.route("/carroCompra/<string:username>", methods=["GET"])
@jwt_required()
def get_carroCompra_username(username):
    """Obtener carro de compras por username"""
    con = con_redis.redis
    x = f'carroCompra {username}'
    conexion = con.get(x)
    if conexion is None:
        con = con_postgres.postgres
        conexion = con.cursor()
        conexion.execute(
            "select * from carroCompra where comprador = '{0}' and estado = 'P'".format(username))
        carroCompra = conexion.fetchall()
        conexion.close()
        return jsonify(carroCompra[0])
    else:
        print(conexion.decode("utf-8"))
        return jsonify(eval(conexion.decode("utf-8"))[0])


@rutas.route("/carroCompra", methods=["POST"])
@jwt_required()
def post_carroCompra():
    """Crear carro de compras"""
    comprador = request.json.get("comprador", None)
    fecha = request.json.get("fecha", None)
    con = con_redis.redis
    x = f'carroCompra {comprador}'
    conexion = con.get(x)
    if conexion is None:
        con = con_postgres.postgres
        conexion = con.cursor()
        conexion.execute(
            "select * from carroCompra where comprador = '{0}' and estado = 'P'".format(comprador))
        carroCompra = conexion.fetchall()
        if len(carroCompra) == 0:
            conexion.execute("insert into carroCompra (comprador, cantidad, estado, fecha) values ('{0}', {1}, '{2}', '{3}')".format(
                comprador, 1, 'P', fecha))
            con.commit()
            conexion.close()
            con = con_redis.redis
            con.set(x, str(carroCompra), ex=3600)
            return jsonify(carroCompra[0][0])
        else:
            con = con_redis.redis
            con.set(x,str(carroCompra), ex=3600)
            return jsonify(carroCompra[0][0])
    else:
        print("Retornando de Redis POST Nuevo tiempo")
        con.set(x,str(eval(conexion.decode("utf-8"))), ex=3600)
        return jsonify(eval(conexion.decode("utf-8"))[0][0])

@rutas.route("/carroCompra/<string:username>/<string:id>/abandonar", methods=["PUT"])
@jwt_required()
def put_carroCompra_username(username, id):
    """Actualizar carro de compras por username"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute(
        "select * from carroCompra where comprador ='{0}'".format(username))
    carroCompra = conexion.fetchall()
    comprador = carroCompra[0][0]
    cantidad = carroCompra[0][1]
    fecha = carroCompra[0][3]
    conexion.execute("update carroCompra set comprador = '{0}', cantidad = {1}, estado = '{2}', fecha = '{3}' where id_carro = {4}".format(
        comprador, cantidad, 'A', fecha, id))
    con.commit()
    conexion.close()
    return jsonify({"msg": "carro de compras actualizado"})


@rutas.route("/carroCompra/<string:username>/<string:id>", methods=["DELETE"])
@jwt_required()
def delete_carroCompra_username(username, id):
    """Eliminar carro de compras por username"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute(
        "delete from carroCompra where id_carroCompra = {0}".format(id))
    con.commit()
    conexion.close()
    return jsonify({"msg": "carro de compras eliminado"})
