secret_number = 777

numero=int(input(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
"""))

while numero !=secret_number:
    print("JAJAJ, estas metido en un pozo de mierda infinito")
    numero=int(input("otro numero: "))
print("WELL DONE! YOU ARE FREE...")    
