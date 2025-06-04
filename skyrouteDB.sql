-- Crear base de datos
CREATE DATABASE IF NOT EXISTS skyrouteDB;
USE skyrouteDB;

-- Tabla: clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    cuit VARCHAR(11) NOT NULL,
    razon_social VARCHAR(100),
    email VARCHAR(50)
);

-- Tabla: destinos
CREATE TABLE IF NOT EXISTS destinos (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(50),
    pais VARCHAR(50),
    costo_base DECIMAL(10,2)
);

-- Tabla: ventas
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_destino INT,
    fecha_venta DATETIME,
    costo_total DECIMAL(10,2),
    estado_venta VARCHAR(20),
    fecha_anulacion DATETIME,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);

-- datos de ejemplo
INSERT INTO clientes (cuit, razon_social, email) VALUES
('11111111111', 'Turismo cordobes SA', 'viajes.CBA@cba.com'),
('22222222222', 'Por el mundo SRL', 'info@porelmundo.com'),
('33333333333', 'Viaja conmigo SRL', 'contacto@viajaconmigo.com');

INSERT INTO destinos (ciudad, pais, costo_base) VALUES
('Mendoza', 'Argentina', 65000.00),
('Misiones', 'Argentina', 40000.00),
('Salta', 'Argentina', 15000.00);

INSERT INTO ventas (id_cliente, id_destino, fecha_venta, costo_total, estado_venta, fecha_anulacion) VALUES
(1, 1, NOW(), 65000.00, 'Activa', NULL),
(2, 2, NOW(), 40000.00, 'Anulada', NOW()),
(3, 3, NOW(), 15000.00, 'Activa', NULL);
