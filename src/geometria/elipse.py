from geometria.geometria import Geometria
from geometria.punto import Punto

class Elipse(Geometria):
    def __init__(self, p, radio_x, radio_y, borde="black", relleno=""):
        self.punto = p
        self.radio_x = radio_x
        self.radio_y = radio_y
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        import math
        return math.pi * self.radio_x * self.radio_y

    def calcular_perimetro(self):
        import math
        # Aproximación de Ramanujan para el perímetro de una elipse
        h = ((self.radio_x - self.radio_y) ** 2) / ((self.radio_x + self.radio_y) ** 2)
        return math.pi * (self.radio_x + self.radio_y) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def dibujar(self, canvas):
        canvas.create_oval(
            self.punto.x - self.radio_x, 
            self.punto.y - self.radio_y, 
            self.punto.x + self.radio_x, 
            self.punto.y + self.radio_y, 
            outline=self.borde, 
            fill=self.relleno
        )