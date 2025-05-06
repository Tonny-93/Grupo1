
import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 3 variables diferentes
<<<<<<< HEAD
<<<<<<< HEAD
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
=======

valor1 = input("ingrese el numero")
valor2 = input("ingrese el numero")
valor3 = input("ingrese numero")
>>>>>>> 7b53f85948d6fd04522862b8212534ef9c01f027
=======
x=(imput"ingrese valor número 1")
y= "ingrese valor número 2"
z=(imput"ingrese valor número 3")
>>>>>>> 16d029df647eb1e531fdb38aa0ec4f0c6c740afa

>>>>>>> 16d029df647eb1e531fdb38aa0ec4f0c6c740afa

#convertir cada variable a entero
cadena = "123"
entero = int(cadena)
print(entero)  # Salida: 123

flotante = 3.14
entero = int(flotante)
print(entero)  # Salida: 3

def operacion(x, y, z):
  """
  Calcula x elevado a y, dividido por z.

  Args:
    x: La base de la potencia.
    y: El exponente de la potencia.
    z: El divisor.

  Returns:
    El resultado de la operación x^y / z, convertido a una cadena de texto.
  """
  resultado = (x ** y) / z
  return str(resultado)

# Ejemplo de uso:
x = 2
y = 3
z = 4
resultado = operacion(x, y, z)
print(resultado)  # Salida: 2.0

"""crear la funcnion operacion 
esta funcion devolera el resultado de:
<<<<<<< HEAD
x elevado a la y, dividido para z """
=======
x elevado a la y, dividido para z
<<<<<<< HEAD
"""
def operacion(x, y, z):
  """
  Calcula x elevado a la y, dividido para z.
=======
""  

y eso es todo


>>>>>>> 16d029df647eb1e531fdb38aa0ec4f0c6c740afa

<<<<<<< HEAD
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
=======
  Args:
      x: El valor base.
      y: El valor del exponente.
      z: El valor del divisor.

  Returns:
      El resultado de x elevado a la y, dividido para z.
  """
>>>>>>> 7b53f85948d6fd04522862b8212534ef9c01f027
  return x**y / z

resultado = operacion(x,y,z)
#convertir este resutado en string
def operacion(x, y, z):
  """
  Calcula x elevado a y, dividido por z.
<<<<<<< HEAD

  Args:
    x: La base de la potencia.
    y: El exponente de la potencia.
    z: El divisor.

  Returns:
    El resultado de la operación x^y / z, convertido a una cadena de texto.
  """
  resultado = (x ** y) / z
  return str(resultado)

# Ejemplo de uso:
x = 2
y = 3
z = 4
resultado = operacion(x, y, z)
print(resultado)  # Salida: 2.0

=======
>>>>>>> 7b53f85948d6fd04522862b8212534ef9c01f027

  Args:
    x: La base de la potencia.
    y: El exponente de la potencia.
    z: El divisor.

  Returns:
    El resultado de la operación x^y / z, convertido a una cadena de texto.
  """
  resultado = (x ** y) / z
  return str(resultado)

# Ejemplo de uso:
x = 2
y = 3
z = 4
resultado = operacion(x, y, z)
print(resultado)  # Salida: 2.0
#mostrar el resultado en el qr
img = qrcode.make(resultado)
type(img)  # qrcode.image.pil.PilImage
img.save("resultado.png")
