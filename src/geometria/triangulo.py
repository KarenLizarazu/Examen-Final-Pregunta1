from geometria.geometria import Geometria
from geometria.punto import Punto

class Triangulo(Geometria):
    def __init__(self, p1, p2, p3, borde="black", relleno=""):
        self.puntos = [p1, p2, p3]
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        # Usar la fórmula de Herón para calcular el área
        a = self.distancia(self.puntos[0], self.puntos[1])
        b = self.distancia(self.puntos[1], self.puntos[2])
        c = self.distancia(self.puntos[2], self.puntos[0])
        
        s = (a + b + c) / 2  # Semiperímetro
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Fórmula de Herón

    def calcular_perimetro(self):
        a = self.distancia(self.puntos[0], self.puntos[1])
        b = self.distancia(self.puntos[1], self.puntos[2])
        c = self.distancia(self.puntos[2], self.puntos[0])
        return a + b + c

    def distancia(self, p1, p2):
        """Calcula la distancia entre dos puntos."""
        return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

    def dibujar(self, canvas):
        canvas.create_polygon(
            [(p.x, p.y) for p in self.puntos],
            outline=self.borde,
            fill=self.relleno,
            width=2
        )