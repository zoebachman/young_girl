# import PyPDF2

# pdfFileObj = open('jeune-fille.pdf', 'rb') #what's rb? > "read binary"
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# pageObj = pdfReader.getPage(5)
# text = pageObj.extractText()
# print text

import textract
import subprocess

text = textract.process('jeune-fille.pdf',  method='pdfminer')
# text = textract.process('path/to/a.pdf', method='pdfminer')

print text
