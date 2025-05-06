
import qrcode
#pedir al usuario que ingrese 3 valores y almacenarlos en 3 variables diferentes
x=(imput"ingrese valor número 1")
y= "ingrese valor número 2"
z=(imput"ingrese valor número 3")


#convertir cada variable a entero



"""
crear la funcnion operacion 
esta funcion devolera el resultado de:
x elevado a la y, dividido para z
""  

y eso es todo




resultado = operacion(x,y,z)
#convertir este resutado en string

#mostrar el resultado en el qr
img = qrcode.make(resultado)
type(img)  # qrcode.image.pil.PilImage
img.save("resultado.png")
