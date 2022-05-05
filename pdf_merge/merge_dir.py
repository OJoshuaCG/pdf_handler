from PyPDF2 import PdfFileMerger
import os

dirDestino = '.res'
# Obtenemos todos los archivos que su extension sea vacia (si son vacias, son carpetas)
carpetas = [archivo for archivo in os.listdir('./') if os.path.splitext(archivo)[1] == ""]


# Eliminamos de la lista la carpeta destino
try:
    if carpetas.index(dirDestino) > -1:
        carpetas.remove(dirDestino)

# Pero si no esta en la lista, la tenemos que crear
except:
    os.mkdir(dirDestino)

for c in carpetas:
    # Seleccionamos todos los archivos pdf (solo pdf)
    pdfs = [archivo for archivo in os.listdir('./'+c) if archivo.endswith(".pdf")]

    # Si no habia pdf, amonos pa mi casa
    if pdfs == []:        
        continue
    
    fusionador = PdfFileMerger()
    
    for pdf in pdfs:
        pdf = "./{}/{}".format(c, pdf)
        fusionador.append(open(pdf, 'rb'))

    destino = "./{}/{}.pdf".format(dirDestino, c)    
    with open(destino, 'wb') as salida:
        fusionador.write(salida)
    



