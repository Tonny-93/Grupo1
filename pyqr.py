import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 3 variables diferentes



#convertir cada variable a entero



"""
crear la funcnion operacion 
esta funcion devolera el resultado de:
x elevado a la y, dividido para z
"""


resultado = operacion(x,y,z)
#convertir este resutado en string

#mostrar el resultado en el qr
img = qrcode.make(resultado)
type(img)  # qrcode.image.pil.PilImage
img.save("resultado.png")


 valor1 = imput("ingresar el numero")
 valor2 = input("ingresar el numero")
 valor3 = input("ingresar el numero")


def operacion(x, y, z)

calcula x, elevado a la y, divido por z.

x: la base de la potencia
y: elevado
z: divisor



 return:
  operacion de x^y / z, convertido a una potencia de texto.

 """

resultado = (x**y) / z
 return str(resultado)


