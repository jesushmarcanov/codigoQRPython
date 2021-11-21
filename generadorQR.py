#Importamos la Librería qrcode
import qrcode
#Le indicamos al programa el nombre del ardhivo (nombreArchivo) y la url que queremos guardar (textoQr)
nombreArchivo = input("Dime el nombre del archivo sin la extensión ")
textoQr = input("Dime el texto o enlace para el código QR ")
#Creamos el  código QR y lo guardamos en la variable imagen
imagen = qrcode.make(textoQr)
#Abrimos el archivo que viene en la variable nombreArchivo
fichero = open(nombreArchivo+".png", "wb")
#Guardamos la imagen en el archivo
imagen.save(fichero)
#Cerramos el archivo
fichero.close()
#Le indicamos la usuario que el código ha sido generado con exito y le decimos donde está guardado
print("El Código QR ha sido generado")
print("El archivo está guardado en la carpeta del script")