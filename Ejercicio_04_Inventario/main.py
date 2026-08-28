class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, cantidad: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self) -> str:
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def modificar_cantidad(self, codigo: str, nueva_cantidad: int):
        p = self.buscar_producto(codigo)
        if p:
            p.cantidad = nueva_cantidad
            print("Cantidad modificada.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, codigo: str):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def calcular_valor_total(self) -> float:
        return sum(p.precio * p.cantidad for p in self.productos)


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto\n2. Modificar cantidad\n3. Buscar producto\n4. Calcular valor total del inventario\n5. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            precio = float(input("Precio: "))
            cant = int(input("Cantidad: "))
            inventario.agregar_producto(Producto(codigo, nombre, precio, cant))
        elif opcion == "2":
            codigo = input("Código del producto: ").strip()
            cant = int(input("Nueva cantidad: "))
            inventario.modificar_cantidad(codigo, cant)
        elif opcion == "3":
            codigo = input("Código del producto: ").strip()
            p = inventario.buscar_producto(codigo)
            if p:
                print(p)
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            print(f"Valor total del inventario: ${inventario.calcular_valor_total():.2f}")
        elif opcion == "5":
            break


if __name__ == "__main__":
    menu()
