class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f}"


class Cliente:
    def __init__(self, identificacion: str, nombre: str):
        self.identificacion = identificacion
        self.nombre = nombre

    def __str__(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre}"


class DetalleVenta:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self) -> float:
        return self.producto.precio * self.cantidad


class Venta:
    def __init__(self, cliente: Cliente, porcentaje_impuesto: float = 19.0):
        self.cliente = cliente
        self.detalles = []
        self.porcentaje_impuesto = porcentaje_impuesto

    def agregar_producto(self, producto: Producto, cantidad: int):
        self.detalles.append(DetalleVenta(producto, cantidad))

    def calcular_subtotal(self) -> float:
        return sum(d.calcular_subtotal() for d in self.detalles)

    def calcular_impuesto(self) -> float:
        return self.calcular_subtotal() * (self.porcentaje_impuesto / 100.0)

    def calcular_total(self) -> float:
        return self.calcular_subtotal() + self.calcular_impuesto()

    def mostrar_factura(self):
        print("\n--- FACTURA DE VENTA ---")
        print(f"Cliente: {self.cliente.nombre} (ID: {self.cliente.identificacion})")
        print("Productos:")
        for d in self.detalles:
            print(f"  - {d.producto.nombre} x{d.cantidad} | Subtotal: ${d.calcular_subtotal():.2f}")
        print(f"Subtotal: ${self.calcular_subtotal():.2f}")
        print(f"Impuesto ({self.porcentaje_impuesto}%): ${self.calcular_impuesto():.2f}")
        print(f"Total: ${self.calcular_total():.2f}")


def menu():
    productos = []
    clientes = []

    while True:
        print("\n1. Registrar producto\n2. Registrar cliente\n3. Realizar venta y mostrar factura\n4. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cod = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            precio = float(input("Precio: "))
            productos.append(Producto(cod, nombre, precio))
        elif opcion == "2":
            ide = input("Identificación: ").strip()
            nombre = input("Nombre: ").strip()
            clientes.append(Cliente(ide, nombre))
        elif opcion == "3":
            ide = input("ID del cliente: ").strip()
            cliente = next((c for c in clientes if c.identificacion == ide), None)
            if not cliente:
                print("Cliente no encontrado.")
                continue

            pct = float(input("Porcentaje de impuesto (ej. 19): ") or 19)
            venta = Venta(cliente, pct)

            while True:
                cod = input("Código del producto a vender (o 'fin'): ").strip()
                if cod.lower() == "fin":
                    break
                p = next((prod for prod in productos if prod.codigo == cod), None)
                if p:
                    cant = int(input(f"Cantidad de {p.nombre}: "))
                    venta.agregar_producto(p, cant)
                else:
                    print("Producto no encontrado.")

            if venta.detalles:
                venta.mostrar_factura()
            else:
                print("Venta cancelada (sin productos).")
        elif opcion == "4":
            break


if __name__ == "__main__":
    menu()
