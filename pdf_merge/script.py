from PyPDF2 import PdfFileMerger
import os

def carpetaDestino(lista, carpeta, path="."):    
    try:
        if lista.index(carpeta) > -1:
            lista.remove(carpeta)
    except:
        os.mkdir(path+'/'+carpeta)
    finally:
        return lista


def mergePDF(pdfs, origen, destino, nombreDestino):
    fusionador = PdfFileMerger()
    try:
        for pdf in pdfs:
            pdf = "./{}/{}".format(origen, pdf)
            fusionador.append(open(pdf, 'rb'))

        destino = "./{}/{}.pdf".format(destino, nombreDestino)
        with open(destino, 'wb') as salida:
            fusionador.write(salida)
        print('Listo!  ', nombreDestino)
    except:
        print('-----> ERROR!!!   ', nombreDestino)

print("Iniciando...")
dirDestino = '.res'
carpetas = [archivo for archivo in os.listdir('./') if os.path.splitext(archivo)[1] == ""]
carpetas = carpetaDestino(carpetas, dirDestino)

for c in carpetas:
    path = './'+c #+'/'
    subcarpetas = [_.name for _ in os.scandir(path) if _.is_dir()]
    
    # with os.scandir('./'+c+'/') as subcarpetas:
    #     subcarpetas = [subc.name for subc in subcarpetas if not(subc.is_file())]
    
    # subcarpetas = [subc for subc in os.listdir('./'+c+'/') if os.path.splitext(subc)[1] == ""]
    subcarpetas = carpetaDestino(subcarpetas, dirDestino, c)
    if(subcarpetas == []):
        continue
    
    for sc in subcarpetas:
        path = './'+c+'/'+sc # +'/' # './'+c+'/'+sc
        pdfs = [archivo for archivo in os.listdir(path) if archivo.endswith(".pdf")]
        
        if(pdfs == []):
            continue
        
        origen = "{}/{}".format(c, sc)
        destino = "{}/{}".format(c, dirDestino)
        nombreDestino = sc
        mergePDF(pdfs, origen, destino, nombreDestino)
    
    path = './'+c+'/'+dirDestino # +'/'    # './'+c+'/'+dirDestino
    pdfs = [archivo for archivo in os.listdir(path) if archivo.endswith(".pdf")]
    origen = "{}/{}".format(c, dirDestino)
    destino = dirDestino
    nombreDestino = c
    mergePDF(pdfs, origen, destino, nombreDestino)

print("---- Finalizado!!! ----")
