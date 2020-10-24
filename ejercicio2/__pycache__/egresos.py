class egresos:
    def __init__(self):
        self.montoTotal = 0
        self.totalTransacciones = 0

    def aumentarEgresos(self, egresos):
        self.montoTotal = self.montoTotal + egresos
        self.totalTransacciones += 1
        return self.montoTotal

    def getMontoTotal(self):
        total = self.montoTotal
        return total

   