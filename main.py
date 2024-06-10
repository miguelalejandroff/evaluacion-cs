from ProductoDTO import ProductoDTO 
from ProductoDB import ProductoDB
from tabulate import tabulate

def crear_producto(db):
    try:
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        categoria = input("Categoría: ")
        producto = ProductoDTO(nombre=nombre, descripcion=descripcion, precio=precio, cantidad=cantidad, categoria=categoria)
        db.add_producto(producto)
        print("Producto creado con éxito.")
    except ValueError as e:
        print(f"Error: {e}")

def ver_producto(db):
    try:
        producto_id = input("ID del Producto: ")
        if not producto_id:
            raise ValueError("Debe ingresar un ID de producto.")
        producto_id = int(producto_id)
        producto = db.get_producto(producto_id)
        if producto:
            headers = ["ID", "Nombre", "Descripción", "Precio", "Cantidad", "Categoría"]
            table = [[producto.id, producto.nombre, producto.descripcion, producto.precio, producto.cantidad, producto.categoria]]
            print(tabulate(table, headers, tablefmt="pretty"))
        else:
            print("Producto no encontrado.")
    except ValueError as e:
        print(f"Error: {e}")

def actualizar_producto(db):
    try:
        producto_id = input("ID del Producto: ")
        if not producto_id:
            raise ValueError("Debe ingresar un ID de producto.")
        producto_id = int(producto_id)
        producto = db.get_producto(producto_id)
        if producto:
            print(f"Nuevo Nombre (actual: {producto.nombre}): ", end="")
            nombre = input().strip() or producto.nombre

            print(f"Nueva Descripción (actual: {producto.descripcion}): ", end="")
            descripcion = input().strip() or producto.descripcion

            print(f"Nuevo Precio (actual: {producto.precio}): ", end="")
            try:
                precio = input().strip()
                precio = float(precio) if precio else producto.precio
            except ValueError:
                precio = producto.precio

            print(f"Nueva Cantidad (actual: {producto.cantidad}): ", end="")
            try:
                cantidad = input().strip()
                cantidad = int(cantidad) if cantidad else producto.cantidad
            except ValueError:
                cantidad = producto.cantidad

            print(f"Nueva Categoría (actual: {producto.categoria}): ", end="")
            categoria = input().strip() or producto.categoria

            producto_actualizado = ProductoDTO(id=producto_id, nombre=nombre, descripcion=descripcion, precio=precio, cantidad=cantidad, categoria=categoria)
            db.update_producto(producto_actualizado)
            print("Producto actualizado con éxito.")
        else:
            print("Producto no encontrado.")
    except ValueError as e:
        print(f"Error: {e}")

def eliminar_producto(db):
    try:
        producto_id = input("ID del Producto: ")
        if not producto_id:
            raise ValueError("Debe ingresar un ID de producto.")
        producto_id = int(producto_id)
        producto = db.get_producto(producto_id)
        if producto:
            db.delete_producto(producto_id)
            print("Producto eliminado con éxito.")
        else:
            print("Producto no encontrado.")
    except ValueError as e:
        print(f"Error: {e}")

def listar_productos(db):
    productos = db.list_productos()
    if productos:
        headers = ["ID", "Nombre", "Descripción", "Precio", "Cantidad", "Categoría"]
        table = [[p.id, p.nombre, p.descripcion, p.precio, p.cantidad, p.categoria] for p in productos]
        print(tabulate(table, headers, tablefmt="pretty"))
    else:
        print("No hay productos disponibles.")

def main():
    db = ProductoDB()
    
    while True:
        print("+----------------------------+")
        print("|  Menú de Operaciones CRUD  |")
        print("+----------------------------+")
        print("| 1. Crear Producto          |")
        print("| 2. Ver Producto            |")
        print("| 3. Actualizar Producto     |")
        print("| 4. Eliminar Producto       |")
        print("| 5. Listar Productos        |")
        print("| 6. Salir                   |")
        print("+----------------------------+")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            crear_producto(db)
        
        elif choice == '2':
            ver_producto(db)
        
        elif choice == '3':
            actualizar_producto(db)
        
        elif choice == '4':
            eliminar_producto(db)
        
        elif choice == '5':
            listar_productos(db)
        
        elif choice == '6':
            break

        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
