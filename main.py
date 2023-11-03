from modelos.cliente import Cliente
from crud import (
    actualizar_cliente,
    obtener_clientes,
    obtener_cliente,
    eliminar_cliente,
    crear_cliente,
)


def pedir_datos(cliente=()):
    nombre = input(f"nombre: ({cliente[1]}) > " if cliente else "Su nombre: ")
    apellido = input(
        f"apellido: ({cliente[2]}) > " if cliente else "Su apellido: ")
    telefono = input(
        f"telefono: ({cliente[3]}) > " if cliente else "Su teléfono: ")
    direccion = input(
        f"dirección: ({cliente[5]}) > " if cliente else "Su dirección: ")
    ciudad = input(
        f"ciudad: ({cliente[6]}) > " if cliente else "Su ciudad: ")

    nuevo_cliente = Cliente(
        nombre if len(nombre) > 0 else cliente[1],
        apellido if len(apellido) > 0 else cliente[2],
        telefono if len(telefono) > 0 else cliente[3],
        direccion if len(direccion) > 0 else cliente[5],
        ciudad if len(ciudad) > 0 else cliente[6])

    email = input(
        f"email: ({cliente[4]}) > ") if cliente else nuevo_cliente.email

    nuevo_cliente.email = email if len(email) > 0 else cliente[4]

    return nuevo_cliente


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    opt = input("Ingresa una opción: ")
    while (opt) not in sorted(opciones):
        print('Opción incorrecta, vuelva a intentarlo.')
        return leer_opcion(opciones)
    return opt


def ejecutar_opcion(opcion, opciones):
    if opciones[opcion][1] == 'crear':
        return crear_cliente(pedir_datos())
    elif opciones[opcion][1] == 'consultar':
        [print(cliente) for cliente in obtener_clientes()]
    elif opciones[opcion][1] == 'actualizar':
        [print(cliente) for cliente in obtener_clientes()]
        while True:
            id = int(input("Selecciona el ID del cliente para actualizar: "))
            ids = [record[0] for record in obtener_clientes()]
            if id in ids:
                datos_actualizados = pedir_datos(obtener_cliente(id))
                actualizar_cliente(datos_actualizados, id)
                break
            else:
                print("id no válido")
                continue
    elif opciones[opcion][1] == 'eliminar':
        [print(cliente) for cliente in obtener_clientes()]
        while True:
            id = int(input("Selecciona el ID del cliente para eliminar: "))
            ids = [record[0] for record in obtener_clientes()]
            if id in ids:
                eliminar_cliente(id)
                break
            else:
                print("id no válido")
                continue
    elif opciones[opcion][1] == 'salir':
        print("Gracias por usar el programa")
        exit()
    else:
        print("Opción no disponible")


def menu():
    opciones = {
        '1': ('Crear un cliente', 'crear'),
        '2': ('Consultar clientes', 'consultar'),
        '3': ('Actualizar a un cliente', 'actualizar'),
        '4': ('Eliminar a un cliente', 'eliminar'),
        '5': ('Salir del programa', 'salir'),
    }
    mostrar_menu(opciones)
    opcion = leer_opcion(opciones)
    ejecutar_opcion(opcion, opciones)
    repetir = input("¿Quieres realizar alguna otra operación? (S/N): ")
    if repetir.upper() == "S":
        menu()
    else:
        exit()


if __name__ == '__main__':
    menu()
