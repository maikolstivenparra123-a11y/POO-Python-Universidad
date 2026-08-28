class Habitacion:
    def __init__(self, numero: int, tipo: str, precio_noche: float):
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.disponible = True

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación N° {self.numero} ({self.tipo}) - ${self.precio_noche:.2f}/noche | Estado: {estado}"


class Cliente:
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Cédula: {self.cedula} | Nombre: {self.nombre}"


class Reserva:
    def __init__(self, cliente: Cliente, habitacion: Habitacion, dias: int):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.activa = True
        self.habitacion.disponible = False

    def calcular_costo(self) -> float:
        return self.habitacion.precio_noche * self.dias

    def cancelar(self):
        self.activa = False
        self.habitacion.disponible = True

    def __str__(self) -> str:
        estado = "Activa" if self.activa else "Cancelada"
        return f"Cliente: {self.cliente.nombre} | Habitación: {self.habitacion.numero} | Días: {self.dias} | Costo: ${self.calcular_costo():.2f} | Estado: {estado}"


class Hotel:
    def __init__(self):
        self.clientes = []
        self.habitaciones = []
        self.reservas = []

    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def registrar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def buscar_cliente(self, cedula: str):
        for c in self.clientes:
            if c.cedula == cedula:
                return c
        return None

    def buscar_habitacion(self, numero: int):
        for h in self.habitaciones:
            if h.numero == numero:
                return h
        return None

    def consultar_disponibles(self):
        disponibles = [h for h in self.habitaciones if h.disponible]
        if not disponibles:
            print("No hay habitaciones disponibles.")
        for h in disponibles:
            print(h)

    def realizar_reserva(self, cedula: str, num_hab: int, dias: int):
        cliente = self.buscar_cliente(cedula)
        hab = self.buscar_habitacion(num_hab)
        if cliente and hab and hab.disponible:
            r = Reserva(cliente, hab, dias)
            self.reservas.append(r)
            print(f"Reserva realizada. Costo total de estadía: ${r.calcular_costo():.2f}")
        else:
            print("No se pudo realizar la reserva.")

    def cancelar_reserva(self, cedula: str, num_hab: int):
        for r in self.reservas:
            if r.cliente.cedula == cedula and r.habitacion.numero == num_hab and r.activa:
                r.cancelar()
                print("Reserva cancelada.")
                return
        print("Reserva no encontrada.")


def menu():
    hotel = Hotel()
    while True:
        print("\n1. Registrar cliente\n2. Registrar habitación\n3. Consultar habitaciones disponibles\n4. Realizar reserva\n5. Cancelar reserva\n6. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cedula = input("Cédula: ").strip()
            nombre = input("Nombre: ").strip()
            hotel.registrar_cliente(Cliente(cedula, nombre))
        elif opcion == "2":
            num = int(input("Número de habitación: "))
            tipo = input("Tipo: ").strip()
            precio = float(input("Precio por noche: "))
            hotel.registrar_habitacion(Habitacion(num, tipo, precio))
        elif opcion == "3":
            hotel.consultar_disponibles()
        elif opcion == "4":
            cedula = input("Cédula del cliente: ").strip()
            num = int(input("Número de habitación: "))
            dias = int(input("Días de estadía: "))
            hotel.realizar_reserva(cedula, num, dias)
        elif opcion == "5":
            cedula = input("Cédula del cliente: ").strip()
            num = int(input("Número de habitación: "))
            hotel.cancelar_reserva(cedula, num)
        elif opcion == "6":
            break


if __name__ == "__main__":
    menu()
