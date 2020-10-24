class ingresos:
    def __init__(self):
        self.montoTotal = 0
        self.totalTransacciones = 0

    def aumentarIngresos(self, ingresos):
        self.montoTotal = self.montoTotal + ingresos
        self.totalTransacciones =+ 1
        return self.montoTotal

    def getMontoTotal(self):
        total = self.montoTotal
        return total

   