import sqlite3

from sqlite3 import Error


def conexion_bd():
    try:
        con = sqlite3.connect("clientes.db")
        return con
    except Error as e:
        print("Error: ", e)


def ejecutar_query(sql, params=''):
    with conexion_bd() as con:
        cursor = con.cursor()
        try:
            return cursor.execute(sql, params)
        except Error as e:
            print("Error: ", e)


with open('db/schema.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    ejecutar_query(sql_script)
