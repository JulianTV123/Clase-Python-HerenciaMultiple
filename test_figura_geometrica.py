from Cuadrado import Cuadrado
# from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

# figura = FiguraGeometrica()

print('Creacion Objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado = 5, color='rojo')
cuadrado1.alto = -10
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion Objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho = 5, alto = 8, color = 'Verde')
rectangulo1.ancho = 15
print(f'Calculo del area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

print(Cuadrado.mro())
