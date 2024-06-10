import unittest
from ProductoDB import ProductoDB
from ProductoDTO import ProductoDTO

class TestProductoDB(unittest.TestCase):
    
    def setUp(self):
        self.db = ProductoDB(":memory:")
        print("")
        
    # Pruebas Unitarias
    def test_add_producto(self):
        producto = ProductoDTO(nombre="Producto1", descripcion="Descripción1", precio=10.99, cantidad=100, categoria="Categoría1")
        self.db.add_producto(producto)
        result = self.db.get_producto(1)
        self.assertIsNotNone(result, "Error: El producto debería haber sido añadido")
        self.assertEqual(result.nombre, "Producto1", "Error: El nombre del producto no coincide")
        print("Prueba de añadir producto completada exitosamente.")

    def test_update_producto(self):
        producto = ProductoDTO(nombre="Producto2", descripcion="Descripción2", precio=20.99, cantidad=200, categoria="Categoría2")
        self.db.add_producto(producto)
        producto_actualizado = ProductoDTO(id=1, nombre="Producto2_Updated", descripcion="Descripción2_Updated", precio=25.99, cantidad=250, categoria="Categoría2_Updated")
        self.db.update_producto(producto_actualizado)
        result = self.db.get_producto(1)
        self.assertEqual(result.nombre, "Producto2_Updated", "Error: El nombre del producto no se ha actualizado correctamente")
        print("Prueba de actualizar producto completada exitosamente.")
        
    def test_delete_producto(self):
        producto = ProductoDTO(nombre="Producto3", descripcion="Descripción3", precio=30.99, cantidad=300, categoria="Categoría3")
        self.db.add_producto(producto)
        self.db.delete_producto(1)
        result = self.db.get_producto(1)
        self.assertIsNone(result, "Error: El producto debería haber sido eliminado")
        print("Prueba de eliminar producto completada exitosamente.")
        
    def test_list_productos(self):
        producto1 = ProductoDTO(nombre="Producto4", descripcion="Descripción4", precio=40.99, cantidad=400, categoria="Categoría4")
        producto2 = ProductoDTO(nombre="Producto5", descripcion="Descripción5", precio=50.99, cantidad=500, categoria="Categoría5")
        self.db.add_producto(producto1)
        self.db.add_producto(producto2)
        productos = self.db.list_productos()
        self.assertEqual(len(productos), 2, "Error: El número de productos en la lista no es el esperado")
        print("Prueba de listar productos completada exitosamente.")
    
    # Pruebas de Validaciones
    def test_validaciones_add_producto(self):
        with self.assertRaises(ValueError, msg="Error: Se debería haber lanzado un ValueError por nombre vacío"):
            producto = ProductoDTO(nombre="", descripcion="Descripción1", precio=10.99, cantidad=100, categoria="Categoría1")
            self.db.add_producto(producto)
        print("Prueba de validación por nombre vacío completada exitosamente.")
       
        with self.assertRaises(ValueError, msg="Error: Se debería haber lanzado un ValueError por precio negativo"):
            producto = ProductoDTO(nombre="Producto1", descripcion="Descripción1", precio=-10.99, cantidad=100, categoria="Categoría1")
            self.db.add_producto(producto)
        print("Prueba de validación por precio negativo completada exitosamente.")
        
        with self.assertRaises(ValueError, msg="Error: Se debería haber lanzado un ValueError por cantidad negativa"):
            producto = ProductoDTO(nombre="Producto1", descripcion="Descripción1", precio=10.99, cantidad=-100, categoria="Categoría1")
            self.db.add_producto(producto)
        print("Prueba de validación por cantidad negativa completada exitosamente.")
        
        with self.assertRaises(ValueError, msg="Error: Se debería haber lanzado un ValueError por categoría vacía"):
            producto = ProductoDTO(nombre="Producto1", descripcion="Descripción1", precio=10.99, cantidad=100, categoria="")
            self.db.add_producto(producto)
        print("Prueba de validación por categoría vacía completada exitosamente.")
    
    def test_validaciones_update_producto(self):
        producto = ProductoDTO(nombre="Producto6", descripcion="Descripción6", precio=60.99, cantidad=600, categoria="Categoría6")
        self.db.add_producto(producto)
        producto = self.db.get_producto(1)
        
        with self.assertRaises(ValueError, msg="Error: Se debería haber lanzado un ValueError por nombre vacío"):
            producto.nombre = ""
            self.db.update_producto(producto)
        print("Prueba de validación por nombre vacío en actualización completada exitosamente.")
        
        with self.assertRaises(ValueError, msg="Error: Se debería haber lanzado un ValueError por precio negativo"):
            producto.precio = -60.99
            self.db.update_producto(producto)
        print("Prueba de validación por precio negativo en actualización completada exitosamente.")
        
        with self.assertRaises(ValueError, msg="Error: Se debería haber lanzado un ValueError por cantidad negativa"):
            producto.cantidad = -600
            self.db.update_producto(producto)
        print("Prueba de validación por cantidad negativa en actualización completada exitosamente.")
        
        with self.assertRaises(ValueError, msg="Error: Se debería haber lanzado un ValueError por categoría vacía"):
            producto.categoria = ""
            self.db.update_producto(producto)
        print("Prueba de validación por categoría vacía en actualización completada exitosamente.")
    
    # Pruebas de Integración
    def test_integracion_crud(self):
        producto = ProductoDTO(nombre="Producto7", descripcion="Descripción7", precio=70.99, cantidad=700, categoria="Categoría7")
        self.db.add_producto(producto)
        
        # Read
        result = self.db.get_producto(1)
        self.assertIsNotNone(result, "Error: El producto debería haber sido añadido")
        self.assertEqual(result.nombre, "Producto7", "Error: El nombre del producto no coincide")
        
        # Update
        producto_actualizado = ProductoDTO(id=1, nombre="Producto7_Updated", descripcion="Descripción7_Updated", precio=75.99, cantidad=750, categoria="Categoría7_Updated")
        self.db.update_producto(producto_actualizado)
        result = self.db.get_producto(1)
        self.assertEqual(result.nombre, "Producto7_Updated", "Error: El nombre del producto no se ha actualizado correctamente")
        
        # Delete
        self.db.delete_producto(1)
        result = self.db.get_producto(1)
        self.assertIsNone(result, "Error: El producto debería haber sido eliminado")
        print("Prueba de integración CRUD completada exitosamente.")
    
    # Pruebas Funcionales
    def test_funcionalidades_consola(self):
        # Simular el flujo de trabajo de la consola
        producto = ProductoDTO(nombre="Producto8", descripcion="Descripción8", precio=80.99, cantidad=800, categoria="Categoría8")
        self.db.add_producto(producto)
        
        # Listar Productos
        productos = self.db.list_productos()
        self.assertEqual(len(productos), 1, "Error: El número de productos en la lista no es el esperado")
        self.assertEqual(productos[0].nombre, "Producto8", "Error: El nombre del producto no coincide")
        
        # Actualizar Producto
        producto_actualizado = ProductoDTO(id=1, nombre="Producto8_Updated", descripcion="Descripción8_Updated", precio=85.99, cantidad=850, categoria="Categoría8_Updated")
        self.db.update_producto(producto_actualizado)
        result = self.db.get_producto(1)
        self.assertEqual(result.nombre, "Producto8_Updated", "Error: El nombre del producto no se ha actualizado correctamente")
        
        # Eliminar Producto
        self.db.delete_producto(1)
        result = self.db.get_producto(1)
        self.assertIsNone(result, "Error: El producto debería haber sido eliminado")
        print("Prueba de funcionalidades de consola completada exitosamente.")

if __name__ == "__main__":
    unittest.main()
