class CuentaBancaria:
    def __init__(self, titular: str, numero_cuenta: str, saldo: float = 0.0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = max(0.0, saldo)
        self.movimientos = []

    def consignar(self, monto: float):
        if monto > 0:
            self.saldo += monto
            self.movimientos.append(f"Consignación: +${monto:.2f}")
            print("Consignación realizada.")
        else:
            print("Monto inválido.")

    def retirar(self, monto: float):
        if monto <= 0:
            print("Monto inválido.")
        elif monto > self.saldo:
            print("Error: No se pueden realizar retiros superiores al saldo disponible.")
        else:
            self.saldo -= monto
            self.movimientos.append(f"Retiro: -${monto:.2f}")
            print("Retiro realizado.")

    def consultar_saldo(self):
        print(f"Titular: {self.titular} | Cuenta: {self.numero_cuenta} | Saldo: ${self.saldo:.2f}")

    def mostrar_movimientos(self):
        if not self.movimientos:
            print("No hay movimientos registrados.")
        for m in self.movimientos:
            print(m)


def menu():
    titular = input("Titular de la cuenta: ").strip()
    num_cuenta = input("Número de cuenta: ").strip()
    saldo_ini = float(input("Saldo inicial: "))
    cuenta = CuentaBancaria(titular, num_cuenta, saldo_ini)

    while True:
        print("\n1. Consignar\n2. Retirar\n3. Consultar saldo\n4. Mostrar movimientos\n5. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            monto = float(input("Monto a consignar: "))
            cuenta.consignar(monto)
        elif opcion == "2":
            monto = float(input("Monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "3":
            cuenta.consultar_saldo()
        elif opcion == "4":
            cuenta.mostrar_movimientos()
        elif opcion == "5":
            break


if __name__ == "__main__":
    menu()
