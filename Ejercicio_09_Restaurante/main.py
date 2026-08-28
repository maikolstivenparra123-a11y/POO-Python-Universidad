class Plato:
    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f}"


class Cliente:
    def __init__(self, nombre: str, mesa: int):
        self.nombre = nombre
        self.mesa = mesa

    def __str__(self) -> str:
        return f"Cliente: {self.nombre} | Mesa: {self.mesa}"


class Pedido:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.platos = []
        self.estado = "pendiente"

    def agregar_plato(self, plato: Plato):
        self.platos.append(plato)

    def calcular_total(self) -> float:
        return sum(p.precio for p in self.platos)

    def cambiar_estado(self, nuevo_estado: str):
        if nuevo_estado.lower() in ["pendiente", "preparado", "entregado"]:
            self.estado = nuevo_estado.lower()
            print(f"Estado cambiado a: {self.estado}")
        else:
            print("Estado inválido. Use: pendiente, preparado o entregado.")

    def __str__(self) -> str:
        platos_str = ", ".join(p.nombre for p in self.platos) if self.platos else "Sin platos"
        return f"{self.cliente} | Estado: {self.estado} | Platos: [{platos_str}] | Total: ${self.calcular_total():.2f}"


class Restaurante:
    def __init__(self):
        self.menu_platos = []
        self.pedidos = []

    def agregar_plato(self, plato: Plato):
        self.menu_platos.append(plato)

    def consultar_menu(self):
        if not self.menu_platos:
            print("El menú está vacío.")
        for p in self.menu_platos:
            print(p)


def menu():
    restaurante = Restaurante()
    while True:
        print("\n1. Agregar plato al menú\n2. Consultar menú\n3. Crear pedido\n4. Cambiar estado de pedido\n5. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cod = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            precio = float(input("Precio: "))
            restaurante.agregar_plato(Plato(cod, nombre, precio))
        elif opcion == "2":
            restaurante.consultar_menu()
        elif opcion == "3":
            nombre = input("Nombre del cliente: ").strip()
            mesa = int(input("Mesa: "))
            pedido = Pedido(Cliente(nombre, mesa))

            while True:
                cod = input("Código del plato a agregar (o 'fin'): ").strip()
                if cod.lower() == "fin":
                    break
                plato = next((p for p in restaurante.menu_platos if p.codigo == cod), None)
                if plato:
                    pedido.agregar_plato(plato)
                    print("Plato agregado.")
                else:
                    print("Plato no encontrado.")

            restaurante.pedidos.append(pedido)
            print(f"Pedido creado. Total: ${pedido.calcular_total():.2f}")
        elif opcion == "4":
            if not restaurante.pedidos:
                print("No hay pedidos.")
                continue
            for idx, p in enumerate(restaurante.pedidos):
                print(f"[{idx}] {p}")
            idx = int(input("Índice del pedido: "))
            if 0 <= idx < len(restaurante.pedidos):
                nuevo_est = input("Nuevo estado (pendiente/preparado/entregado): ").strip()
                restaurante.pedidos[idx].cambiar_estado(nuevo_est)
        elif opcion == "5":
            break


if __name__ == "__main__":
    menu()
