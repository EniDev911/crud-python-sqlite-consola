from db.conexion import ejecutar_query


def crear_cliente(cliente):
    sql = """
          INSERT INTO clientes
          (nombre, apellido, email, telefono, direccion, ciudad)
          VALUES
          (:nombre, :apellido, :email, :telefono, :direccion, :ciudad)"""
    ejecutar_query(
        sql,
        {
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
            "telefono": cliente.telefono,
            "email": cliente.email,
            "direccion": cliente.direccion,
            "ciudad": cliente.ciudad,
        }
    )


def obtener_clientes():
    return ejecutar_query("SELECT * FROM clientes").fetchall()


def obtener_cliente(id_cliente):
    return ejecutar_query("SELECT * FROM clientes WHERE id=:id",
                          {'id': id_cliente}).fetchone()


def actualizar_cliente(cliente, id_cliente):
    sql = """UPDATE clientes
            SET nombre=:nombre,
                apellido=:apellido,
                telefono=:telefono,
                email=:email,
                direccion=:direccion,
                ciudad=:ciudad
            WHERE id=:id"""
    ejecutar_query(
        sql,
        {
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
            "telefono": cliente.telefono,
            "email": cliente.email,
            "direccion": cliente.direccion,
            "ciudad": cliente.ciudad,
            "id": id_cliente,
        }
    )


def eliminar_cliente(id_cliente):
    sql = "DELETE FROM clientes WHERE id=:id"
    ejecutar_query(sql, {'id': id_cliente})
