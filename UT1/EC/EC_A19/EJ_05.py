class MyappException(Exception):
    def __init__(self,mensaje_err: str, code: int, ) -> None:
        self.code = code
        super().__init__(f'Error {code}: {mensaje_err}')

class InvalidPriceError(MyappException):
    def __init__(self, mensaje_err: str):
        super().__init__(mensaje_err, 100)
        self.mensaje_err = 'Error: Se esperaba un número'

class InvalidDiscountError(MyappException):
    def __init__(self, mensaje_err: str):
        super().__init__(mensaje_err, 101)
        self.mensaje_err = 'Error: El descuento debe estar entre 0 y 100'

def calcular_descuento(precio_original: int, porcentaje_descuento: int) -> int | None:
    try:
        if isinstance(precio_original, int):
            raise InvalidPriceError("El precio debe ser un número positivo.")
        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            raise InvalidDiscountError("El descuento debe estar en el rango de 0 a 100.")

        precio_final = precio_original - (precio_original * porcentaje_descuento / 100)
        return precio_final

    except (InvalidPriceError, InvalidDiscountError) as e:
        print(f"Se ha producido un error: {e}")
        return None

def main():
    precio_final = calcular_descuento(100, 10)
    print(f"Precio final 1: {precio_final}")

    precio_final = calcular_descuento(100, -10)  # Error: El descuento debe estar en el rango de 0 a 100
    precio_final = calcular_descuento(100, 110)  # Error: El descuento debe estar en el rango de 0 a 100
    precio_final = calcular_descuento("100", 10)  # Error: Se esperaba un número


if __name__ == '__main__':
    main()