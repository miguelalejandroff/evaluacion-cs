import sqlite3
from ProductoDTO import ProductoDTO

class ProductoDB:
    def __init__(self, db_name="productos.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        try:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE,
                    descripcion TEXT,
                    precio REAL NOT NULL CHECK(precio > 0),
                    cantidad INTEGER NOT NULL CHECK(cantidad >= 0),
                    categoria TEXT NOT NULL
                );
            ''')
        except Exception as e:
            print(f"Error creating table: {e}")

    def validate_producto(self, producto_dto):
        if not producto_dto.nombre:
            raise ValueError("El nombre del producto es obligatorio.")
        if producto_dto.precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if producto_dto.cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero positivo.")
        if not producto_dto.categoria:
            raise ValueError("La categoría del producto es obligatoria.")

    def add_producto(self, producto_dto):
        self.validate_producto(producto_dto)
        try:
            self.conn.execute('''
                INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria)
                VALUES (?, ?, ?, ?, ?)
            ''', (producto_dto.nombre, producto_dto.descripcion, producto_dto.precio, producto_dto.cantidad, producto_dto.categoria))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError("El nombre del producto debe ser único.") from e

    def get_producto(self, producto_id):
        cursor = self.conn.execute('SELECT * FROM productos WHERE id=?', (producto_id,))
        row = cursor.fetchone()
        if row:
            return ProductoDTO(*row)
        return None

    def update_producto(self, producto_dto):
        self.validate_producto(producto_dto)
        try:
            self.conn.execute('''
                UPDATE productos
                SET nombre=?, descripcion=?, precio=?, cantidad=?, categoria=?
                WHERE id=?
            ''', (producto_dto.nombre, producto_dto.descripcion, producto_dto.precio, producto_dto.cantidad, producto_dto.categoria, producto_dto.id))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError("El nombre del producto debe ser único.") from e

    def delete_producto(self, producto_id):
        try:
            self.conn.execute('DELETE FROM productos WHERE id=?', (producto_id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error deleting producto: {e}")

    def list_productos(self):
        cursor = self.conn.execute('SELECT * FROM productos')
        return [ProductoDTO(*row) for row in cursor.fetchall()]
