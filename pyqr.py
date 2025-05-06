import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 3 variables diferentes



#convertir cada variable a entero



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
