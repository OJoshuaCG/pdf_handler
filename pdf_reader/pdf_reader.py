from PyPDF2 import PdfFileReader

pdf_document = "beca.pdf"

with open(pdf_document, "rb") as filehandle:
    pdf = PdfFileReader(filehandle)
    info = pdf.getDocumentInfo()
    pages = pdf.getNumPages()
    #print (info)
    #print ("number of pages: %i" % pages)

    stPage = pdf.getPage(0)
    text = stPage.extractText()
    
    arregloTexto = text.split("\n")
    arreglo = []
    
    for i in range(3, len(arregloTexto) - 4, 3 ):
        nombre = arregloTexto[i]
        matricula = arregloTexto[i+1]
        carrera = arregloTexto[i+2]
        arreglo.append((nombre, matricula, carrera))


    #print(text)
    print(format(arreglo))
    


    
    '''
    for page in range(pages):
        actualPage = pdf.getPage(page)
        #print(actualPage)

        text = actualPage.extractText()
        print(text)
    '''
     

    '''
    index = text.find("CELULAR:")
    celular = text[index+8:index+8+10]
    print(celular)
    '''

    