"""Utilizar flask y la conexión con postgresql para acceder a la base de datos de usuarios"""
from flask import Flask, request, jsonify
from conexion import con_postgres
from . import rutas


@rutas.route("/usuario/<string:username>", methods=["GET"])
def get_usuario(username):
    """Obtener usuario"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from usuario where username ='{0}'".format(username))
    usuario = conexion.fetchall()   
    conexion.close()
    return jsonify(usuario)


def auth(username,password):
    """Autenticar usuario"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from usuario where username ='{0}' and contraseña ='{1}'".format(username,password))
    usuario = conexion.fetchall()   
    conexion.close()
    return usuario


@rutas.route("/usuarios", methods=["GET"])
def get_usuarios():
    """Obtener todos los usuarios"""
    con = con_postgres.postgres
    conexion = con.cursor()
    conexion.execute("select * from usuario")
    usuarios = conexion.fetchall()   
    conexion.close()
    return jsonify(usuarios)