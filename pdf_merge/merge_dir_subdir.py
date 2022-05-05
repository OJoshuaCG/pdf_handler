from PyPDF2 import PdfFileMerger
import os

def carpetaDestino(lista, carpeta, path="."):
    # Eliminamos de la lista la carpeta destino
    try:
        if lista.index(carpeta) > -1:
            lista.remove(carpeta)
    # Pero si no esta en la lista, la tenemos que crear
    except:
        os.mkdir(path+'/'+carpeta)
    finally:
        return lista


def mergePDF(pdfs, origen, destino, nombreDestino):
    fusionador = PdfFileMerger()
    for pdf in pdfs:
        pdf = "./{}/{}".format(origen, pdf)
        fusionador.append(open(pdf, 'rb'))

    destino = "./{}/{}.pdf".format(destino, nombreDestino)
    with open(destino, 'wb') as salida:
        fusionador.write(salida)


dirDestino = '.res'
# Obtenemos todos los archivos que su extension sea vacia (si son vacias, son carpetas)
carpetas = [archivo for archivo in os.listdir('./') if os.path.splitext(archivo)[1] == ""]
carpetas = carpetaDestino(carpetas, dirDestino)

for c in carpetas:
    subcarpetas = [subc for subc in os.listdir('./'+c) if os.path.splitext(subc)[1] == ""]  
    subcarpetas = carpetaDestino(subcarpetas, dirDestino, c)

    if(subcarpetas == []):
        continue
    
    for sc in subcarpetas:
        pdfs = [archivo for archivo in os.listdir('./'+c+'/'+sc) if archivo.endswith(".pdf")]
        
        if(pdfs == []):
            continue
        
        origen = "{}/{}".format(c, sc)
        destino = "{}/{}".format(c, dirDestino)
        nombreDestino = sc
        mergePDF(pdfs, origen, destino, nombreDestino)
    
    
    # Juntar todos los archivos resultados 
    pdfs = [archivo for archivo in os.listdir('./'+c+'/'+dirDestino) if archivo.endswith(".pdf")]
    origen = "{}/{}".format(c, dirDestino)
    destino = dirDestino
    nombreDestino = c
    mergePDF(pdfs, origen, destino, nombreDestino)

print("Terminado!")


