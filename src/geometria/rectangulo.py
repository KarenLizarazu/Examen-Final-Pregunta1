# src/geometria/rectangulo.py

from geometria.geometria import Geometria
from geometria.punto import Punto
class Rectangulo(Geometria):
    def __init__(self, p1, p2, borde="black", relleno=""):
        self.punto_inicial = p1
        self.punto_final = p2
        self.borde = borde
        self.relleno = relleno
        self.ladox = abs(self.punto_inicial.x - self.punto_final.x)
        self.ladoy = abs(self.punto_inicial.y - self.punto_final.y)

    def calcular_area(self):
        return self.ladox * self.ladoy

    def calcular_perimetro(self):
        return 2 * self.ladox + 2 * self.ladoy

    def dibujar(self, canvas):
        canvas.create_rectangle(self.punto_inicial.x, self.punto_inicial.y, self.punto_final.x, self.punto_final.y, outline=self.borde, fill=self.relleno)