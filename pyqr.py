
import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 3 variables diferentes
# Pedir al usuario que ingrese el primer valor
valor1 = input("Ingrese el primer valor: ")

# Pedir al usuario que ingrese el segundo valor
valor2 = input("Ingrese el segundo valor: ")

# Pedir al usuario que ingrese el tercer valor
valor3 = input("Ingrese el tercer valor: ")

# (Opcional) Convertir los valores a números si son necesarios para operaciones matemáticas
# valor1 = float(valor1)  # Convierte a número de punto flotante
# valor2 = float(valor2)
# valor3 = float(valor3)

# Ahora puedes usar las variables valor1, valor2 y valor3 para trabajar con los valores ingresados
print("Los valores ingresados son:", valor1, valor2, valor3)


#convertir cada variable a entero
cadena = "123"
entero = int(cadena)
print(entero)  # Salida: 123

flotante = 3.14
entero = int(flotante)
print(entero)  # Salida: 3



"""
crear la funcnion operacion 
esta funcion devolera el resultado de:
x elevado a la y, dividido para z """

def operacion(x, y, z):
  """
  Calcula x elevado a la y, dividido por z.

  Args:
    x: La base de la potencia.
    y: El exponente de la potencia.
    z: El divisor.

  Returns:
    El resultado de x elevado a la y, dividido por z.
  """
  if z == 0:
    return "Error: División por cero."  # Manejo del caso de división por cero
  return x**y / z

resultado = operacion(x,y,z)
#convertir este resutado en string
numero = 123
cadena = str(numero)
print(type(cadena))  # Output: <class 'str'>
print(cadena)  # Output: 123


#mostrar el resultado en el qr
img = qrcode.make(resultado)
type(img)  # qrcode.image.pil.PilImage
img.save("resultado.png")
