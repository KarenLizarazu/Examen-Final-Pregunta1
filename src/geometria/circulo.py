import math
from geometria.geometria import Geometria
from geometria.punto import Punto
class Circulo(Geometria):
    def __init__(self, p, radio, borde="black", relleno=""):
        self.punto = p
        self.radio = radio
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        return 0

    def calcular_perimetro(self):
        return 0

    def dibujar(self, canvas):
        canvas.create_oval(self.punto.x - self.radio, self.punto.y - self.radio, self.punto.x + self.radio, self.punto.y + self.radio, outline=self.borde, fill=self.relleno)
