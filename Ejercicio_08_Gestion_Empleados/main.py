class Empleado:
    def __init__(self, nombre: str, identificacion: str, cargo: str, salario: float):
        self.nombre = nombre
        self.identificacion = identificacion
        self.cargo = cargo
        self.salario = salario

    def calcular_salario(self) -> float:
        return self.salario

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Cargo: {self.cargo} | Salario: ${self.calcular_salario():.2f}"


class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre: str, identificacion: str, cargo: str, salario_fijo: float):
        super().__init__(nombre, identificacion, cargo, salario_fijo)

    def calcular_salario(self) -> float:
        return self.salario


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre: str, identificacion: str, cargo: str, horas: float, valor_hora: float):
        super().__init__(nombre, identificacion, cargo, 0.0)
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self) -> float:
        return self.horas * self.valor_hora


def menu():
    empleados = []
    while True:
        print("\n1. Registrar Empleado Asalariado\n2. Registrar Empleado por Horas\n3. Mostrar información de empleados\n4. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            ide = input("Identificación: ").strip()
            cargo = input("Cargo: ").strip()
            salario = float(input("Salario fijo: "))
            empleados.append(EmpleadoAsalariado(nombre, ide, cargo, salario))
        elif opcion == "2":
            nombre = input("Nombre: ").strip()
            ide = input("Identificación: ").strip()
            cargo = input("Cargo: ").strip()
            horas = float(input("Horas trabajadas: "))
            valor = float(input("Valor por hora: "))
            empleados.append(EmpleadoPorHoras(nombre, ide, cargo, horas, valor))
        elif opcion == "3":
            if not empleados:
                print("No hay empleados registrados.")
            for e in empleados:
                print(e.mostrar_informacion())
        elif opcion == "4":
            break


if __name__ == "__main__":
    menu()
