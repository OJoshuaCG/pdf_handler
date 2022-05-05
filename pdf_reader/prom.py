import PyPDF2
pdfFileObj = open('kardex.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)
print(pdfReader.isEncrypted)

info = pdfReader.documentInfo

#pageObj = pdfReader.getPage(0)
#print(pageObj.extractText())
#print()

for x in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(x)
    txt = pageObj.extractText()
    if(txt != ''):
        print('No es vacio')
    #print(pageObj.extractText())
