CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    cuit VARCHAR(11)
);

CREATE TABLE destinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(50),
    precio DECIMAL(10,2)
);

CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    destino_id INT,
    estado VARCHAR(20),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (destino_id) REFERENCES destinos(id)
);
