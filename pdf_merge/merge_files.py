from PyPDF2 import PdfFileMerger
import os

archivoDestino = 'res.pdf'

# Seleccionamos todos los archivos pdf (solo pdf)
pdfs = [archivo for archivo in os.listdir('./') if archivo.endswith(".pdf")]
       
if pdfs == []:        
    print("No hay pdf que unir")
    exit()

fusionador = PdfFileMerger()

for pdf in pdfs:    
    fusionador.append(open(pdf, 'rb'))

with open(archivoDestino, 'wb') as salida:
    fusionador.write(salida)

print("Union terminado con exito!")