#Herramienta para poder trabajar con PDF's
import pdfplumber

proms = []
# Abro el kardex
pdf = pdfplumber.open('kardex2.pdf')
# Todas las calif estan en la pagina 0 (1)

page = pdf.pages[0]
# Extraemos los datos linea por linea
text = page.extract_text().split('\n')


# Recorremos la tabla del Kardex fila por fila (primera pagina)
for x in range(11, len(text)-2):
  # Obtenemos la informacion de la materia
  materias_info = text[x]
  # Separamos la informacion de la materia por columnas
  data = materias_info.split(' ')
  #print(data)
  
  # Si hay menos de 12 columnas lo ignoramos
  # Porque esta incompleta la fila
  if(len(data) < 12):
    continue # con la siguiente fila
  
  if(data[-6] == '\xa0'):
    break
  
  # Añadimos el promedio a nuestra lista de promedio
  proms.append(int(data[-6]))


page = pdf.pages[1]
text = page.extract_text().split('\n')


# Seguimos recorriendo la tabla del Kardex fila por fila (segunda pagina)
for x in range(5, len(text)-12):
  # Obtenemos la informacion de la materia
  materias_info = text[x]
  # Separamos la informacion de la materia por columnas
  data = materias_info.split(' ')
  #print(data)
  
  # Si hay menos de 12 columnas lo ignoramos
  # Porque esta incompleta la fila
  if(len(data) < 12):
    continue # con la siguiente fila
    
  if(data[-6] == '\xa0'):
    break

  # Añadimos el promedio a nuestra lista de promedio  
  proms.append(int(data[-6]))

# Imprimimos todos los datos
#print(proms)

print("Cantidad: ", len(proms))
print("Suma:     ", sum(proms))
print("Promedio: ", sum(proms)/len(proms))


