class Cliente:
    puntos_por_dolar: int = 1
    def __init__(self, cedula: str, nombre: str, email: str, puntos: int = 0):
        if puntos < 0:
            raise ValueError("Los puntos iniciales no pueden ser negativos.")
        self.cedula = cedula
        self.nombre = nombre
        self.__email = email
        self.puntos = puntos

    def acumular(self, monto_compra: float) -> int:
        if monto_compra <= 0:
            raise ValueError("El monto de la compra debe ser mayor a cero.")
        puntos_ganados = int(monto_compra * Cliente.puntos_por_dolar)
        self.puntos += puntos_ganados
        return puntos_ganados

    def canjear(self, puntos_a_canjear: int) -> bool:
        if puntos_a_canjear <= 0:
            raise ValueError("Los puntos a canjear deben ser mayores a cero.")
        if self.puntos >= puntos_a_canjear:
            self.puntos -= puntos_a_canjear
            return True
        return False

    def get_email(self) -> str:
        return self.__email

    def __str__(self) -> str:
        return f"Cliente: {self.nombre} - Cedula: {self.cedula} - Email: {self.__email} - Puntos: {self.puntos}"

if __name__ == "__main__":
    # Creacion de los 3 clientes
    cliente1 = Cliente(cedula="0928374651", nombre="Liam Castillo", email="liam.castillo@email.com")
    cliente2 = Cliente("0948236500", "Javier Mero", "mero.javier@email.com", puntos=100)
    cliente3 = Cliente("0966879229", "Maritza Rodriguez", "maritza.rodriguez@email.com", puntos=50)

    print("--- ESTADO INICIAL ---")
    print(cliente1)
    print(cliente2)

    print("\n--- REGISTRANDO COMPRAS ---")
    ganados1 = cliente1.acumular(150.50)
    print(f"{cliente1.nombre} ganó {ganados1} puntos")

    ganados2 = cliente2.acumular(80.00)
    print(f"{cliente2.nombre} ganó {ganados2} puntos")

    print("\n--- REALIZANDO CANJES ---")
    exito_canje1 = cliente3.canjear(30)
    print("Canje de 30 puntos para", cliente3.nombre, "exitoso:", exito_canje1)

    exito_canje2 = cliente3.canjear(100)
    print("Canje de 100 puntos para", cliente3.nombre, "exitoso:", exito_canje2)

    print("\n--- PRUEBA DE VALIDACIONES ---")
    for descripcion, accion in [
    ("acumular(-50)", lambda: cliente1.acumular(-50)),
    ("canjear(-20)", lambda: cliente3.canjear(-20)),
    ("canjear(0)", lambda: cliente3.canjear(0)),
    ]:
        try:
            accion()
        except ValueError as e:
            print(f"{descripcion} -> ValueError: {e}")

    print("\n--- ESTADO FINAL ---")
    print(cliente1)
    print(cliente2)
    print(cliente3)