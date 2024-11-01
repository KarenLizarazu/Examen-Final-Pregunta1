
import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo
from geometria.cuadrado import Cuadrado
from geometria.elipse import Elipse
from geometria.punto import Punto
from geometria.triangulo import Triangulo

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    # Crear objetos geométricos
    circulo = Circulo(Punto(350, 550), 40, relleno="purple")
    rectangulo = Rectangulo(Punto(50, 50), Punto(150, 250), "blue", "red")
    cuadrado = Cuadrado(Punto(500, 50), 100, borde="green", relleno="yellow")
    elipse = Elipse(Punto(250, 400), 80, 40, borde="purple", relleno="pink")
    triangulo = Triangulo(Punto(200, 100), Punto(150, 200), Punto(250, 200), relleno="lightgreen")


    # Calcular y mostrar áreas y perímetros
    resultados = [
        f"Área del círculo: {circulo.calcular_area():.2f}, Perímetro del círculo: {circulo.calcular_perimetro():.2f}",
        f"Área del rectángulo: {rectangulo.calcular_area():.2f}, Perímetro del rectángulo: {rectangulo.calcular_perimetro():.2f}",
        f"Área del cuadrado: {cuadrado.calcular_area():.2f}, Perímetro del cuadrado: {cuadrado.calcular_perimetro():.2f}",
        f"Área de la elipse: {elipse.calcular_area():.2f}, Perímetro de la elipse: {elipse.calcular_perimetro():.2f}",
        f"Área del triángulo: {triangulo.calcular_area():.2f}, Perímetro del triángulo: {triangulo.calcular_perimetro():.2f}",
    ]
    
    resultado_label = tk.Label(root, text="\n".join(resultados), font=("Arial", 14), justify=tk.LEFT)
    resultado_label.pack(pady=20)

    # Dibujar figuras
    circulo.dibujar(canvas)
    rectangulo.dibujar(canvas)
    cuadrado.dibujar(canvas)
    elipse.dibujar(canvas)
    triangulo.dibujar(canvas)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()