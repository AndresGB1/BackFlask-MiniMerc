import psycopg2

postgres = psycopg2.connect(
    host="ec2-3-225-213-67.compute-1.amazonaws.com",
    database="dd1jsit7sca899",
    user="vwmlgzrbsknkkc",
    port="5432",
    password="14912582fa76ffafdb62ffdf8dc464814738a9de703028ed73650614854a57fa")

conexion = postgres.cursor()

conexion.execute("select * from usuario")
print(conexion.fetchall())

conexion.close()