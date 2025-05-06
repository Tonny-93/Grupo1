import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 3 variables diferentes

valor1 = input("ingrese el numero")
valor2 = input("ingrese el numero")
valor3 = input("ingrese numero")

#convertir cada variable a entero



"""crear la funcnion operacion 
esta funcion devolera el resultado de:
x elevado a la y, dividido para z
"""
def operacion(x, y, z):
  """
  Calcula x elevado a la y, dividido para z.

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
