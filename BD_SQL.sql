BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "clientes" (
	"id_cliente"	INTEGER,
	"nombre"	VARCHAR(100),
	"apellido"	VARCHAR(100),
	"direccion"	VARCHAR(255),
	"telefono"	VARCHAR(20),
	"email"	VARCHAR(100),
	PRIMARY KEY("id_cliente" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "productos" (
	"id_producto"	INTEGER,
	"nombre"	VARCHAR(100),
	"descripcion"	TEXT,
	"precio"	DECIMAL(10, 2),
	"stock"	INT,
	PRIMARY KEY("id_producto" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ventas" (
	"id_venta"	INTEGER,
	"id_cliente"	INTEGER,
	"id_producto"	INTEGER,
	"cantidad"	INT,
	"fecha_venta"	DATE,
	FOREIGN KEY("id_cliente") REFERENCES "clientes"("id_cliente"),
	FOREIGN KEY("id_producto") REFERENCES "productos"("id_producto"),
	PRIMARY KEY("id_venta" AUTOINCREMENT)
);
INSERT INTO "clientes" ("id_cliente","nombre","apellido","direccion","telefono","email") VALUES (1,'Juan','Perez','Calle 123, Ciudad ABC','123456789','juan@example.com');
INSERT INTO "clientes" ("id_cliente","nombre","apellido","direccion","telefono","email") VALUES (2,'María','Gómez','Avenida XYZ, Pueblo DEF','987654321','maria@example.com');
INSERT INTO "clientes" ("id_cliente","nombre","apellido","direccion","telefono","email") VALUES (3,'Carlos','Martínez','Carrera 456, Villa GHI','456789012','carlos@example.com');
INSERT INTO "clientes" ("id_cliente","nombre","apellido","direccion","telefono","email") VALUES (4,'Luisa','Rodríguez','Calle Principal, Ciudad JKL','789012345','luisa@example.com');
INSERT INTO "clientes" ("id_cliente","nombre","apellido","direccion","telefono","email") VALUES (5,'Ana','Sánchez','Avenida Central, Pueblo MNO','210987654','ana@example.com');
INSERT INTO "clientes" ("id_cliente","nombre","apellido","direccion","telefono","email") VALUES (6,'Pedro','López','Calle Secundaria, Villa PQR','543210987','pedro@example.com');
INSERT INTO "productos" ("id_producto","nombre","descripcion","precio","stock") VALUES (1,'Espada medieval','Espada de acero forjado, réplica de la Edad Media',99.99,20);
INSERT INTO "productos" ("id_producto","nombre","descripcion","precio","stock") VALUES (2,'Arco y flechas','Arco de madera y flechas con puntas de piedra',79.5,15);
INSERT INTO "productos" ("id_producto","nombre","descripcion","precio","stock") VALUES (3,'Daga vikinga','Daga de hierro con empuñadura decorada, estilo vikingo',59.75,10);
INSERT INTO "productos" ("id_producto","nombre","descripcion","precio","stock") VALUES (4,'Mosquete','Mosquete de avancarga con cañón de bronce',149.25,5);
INSERT INTO "productos" ("id_producto","nombre","descripcion","precio","stock") VALUES (5,'Katana samurái','Katana japonesa auténtica, hoja de acero plegado',199.99,8);
INSERT INTO "productos" ("id_producto","nombre","descripcion","precio","stock") VALUES (6,'Ballesta medieval','Ballesta de madera y metal, utilizada en la Edad Media',129,12);
INSERT INTO "ventas" ("id_venta","id_cliente","id_producto","cantidad","fecha_venta") VALUES (1,1,1,2,'2024-05-01');
INSERT INTO "ventas" ("id_venta","id_cliente","id_producto","cantidad","fecha_venta") VALUES (2,2,2,1,'2024-05-15');
INSERT INTO "ventas" ("id_venta","id_cliente","id_producto","cantidad","fecha_venta") VALUES (3,3,3,1,'2024-05-20');
INSERT INTO "ventas" ("id_venta","id_cliente","id_producto","cantidad","fecha_venta") VALUES (4,4,4,3,'2024-05-25');
INSERT INTO "ventas" ("id_venta","id_cliente","id_producto","cantidad","fecha_venta") VALUES (5,5,5,2,'2024-05-28');
INSERT INTO "ventas" ("id_venta","id_cliente","id_producto","cantidad","fecha_venta") VALUES (6,6,6,1,'2024-05-30');
COMMIT;
