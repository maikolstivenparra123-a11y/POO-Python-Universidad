class Vehiculo:
    def __init__(self, marca: str, modelo: str, precio: float):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_informacion(self) -> str:
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Precio: ${self.precio:.2f}"


class Carro(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio: float, numero_puertas: int):
        super().__init__(marca, modelo, precio)
        self.numero_puertas = numero_puertas

    def tocar_bocina(self):
        print("¡Beep beep!")

    def mostrar_informacion(self) -> str:
        return f"[Carro] {super().mostrar_informacion()} | Puertas: {self.numero_puertas}"


class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio: float, cilindraje: int):
        super().__init__(marca, modelo, precio)
        self.cilindraje = cilindraje

    def hacer_caballito(self):
        print("¡Haciendo caballito!")

    def mostrar_informacion(self) -> str:
        return f"[Motocicleta] {super().mostrar_informacion()} | Cilindraje: {self.cilindraje}cc"


def menu():
    vehiculos = []
    while True:
        print("\n1. Registrar Carro\n2. Registrar Motocicleta\n3. Mostrar información de vehículos\n4. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            precio = float(input("Precio: "))
            puertas = int(input("Número de puertas: "))
            vehiculos.append(Carro(marca, modelo, precio, puertas))
        elif opcion == "2":
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            precio = float(input("Precio: "))
            cil = int(input("Cilindraje (cc): "))
            vehiculos.append(Motocicleta(marca, modelo, precio, cil))
        elif opcion == "3":
            if not vehiculos:
                print("No hay vehículos registrados.")
            for v in vehiculos:
                print(v.mostrar_informacion())
        elif opcion == "4":
            break


if __name__ == "__main__":
    menu()
