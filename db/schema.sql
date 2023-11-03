CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    telefono VARCHAR(12) NOT NULL,
    email VARCHAR(50) NOT NULL,
    direccion VARCHAR(100),
    ciudad VARCHAR(50)
);