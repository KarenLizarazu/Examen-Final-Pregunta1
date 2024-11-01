from geometria.geometria import Geometria
from geometria.punto import Punto

class Cuadrado(Geometria):
    def __init__(self, p1, lado, borde="black", relleno=""):
        self.punto_inicial = p1
        self.lado = lado
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

    def dibujar(self, canvas):
        canvas.create_rectangle(
            self.punto_inicial.x, 
            self.punto_inicial.y, 
            self.punto_inicial.x + self.lado, 
            self.punto_inicial.y + self.lado, 
            outline=self.borde, 
            fill=self.relleno
        )