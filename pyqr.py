
import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 3 variables diferentes
<<<<<<< HEAD

valor1 = input("ingrese el numero")
valor2 = input("ingrese el numero")
valor3 = input("ingrese numero")
=======
x=(imput"ingrese valor número 1")
y= "ingrese valor número 2"
z=(imput"ingrese valor número 3")

>>>>>>> 16d029df647eb1e531fdb38aa0ec4f0c6c740afa

#convertir cada variable a entero

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

  Args:
      x: El valor base.
      y: El valor del exponente.
      z: El valor del divisor.

  Returns:
      El resultado de x elevado a la y, dividido para z.
  """
  return x**y / z

resultado = operacion(x,y,z)
#convertir este resutado en string
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
#mostrar el resultado en el qr
img = qrcode.make(resultado)
type(img)  # qrcode.image.pil.PilImage
img.save("resultado.png")
