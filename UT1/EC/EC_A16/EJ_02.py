class Cliente:
    def __init__(self, nombre: str):
        self._titular = nombre


class CuentaBancaria:
    def __init__(self, titular: Cliente, ccc: str):
        self._titular = titular
        self._saldo = 0
        self._ccc = ccc

    def depositar(self, importe: float):
        self._saldo += importe

    def transferencia(self, importe: float, cuenta_destino):
        if self._saldo < importe:
            print(f'No se puede transferir este importe {importe}')
            return
        self._saldo -= importe
        cuenta_destino.depositar(importe)

    def __str__(self):
        return f'Titular: {self._titular} Saldo: {self._saldo}'

if __name__ == '__main__':
    yo = Cliente('Victor jimenez')
    miguel = Cliente('Miguel Romero')

    micuenta = CuentaBancaria('yo', '78287457878')
    cuantaMiguel = CuentaBancaria('Miguel', '254185935')
    micuenta.depositar(1985)
    print(micuenta)
    micuenta.transferencia(620, cuantaMiguel)
    print(micuenta)
