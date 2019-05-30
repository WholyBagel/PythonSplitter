# pdf_splitter.py
 
import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter
 
 
def pdf_splitter(path, title, min, max):
    
    fileNumber = path[0:len(path)-4]
    with open(path, 'rb') as infile:
        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        for page in range(min, max):
            writer.addPage(reader.getPage(page))
        output_filename = 'Temp/{}-{}.pdf'.format(fileNumber, title)
        with open(output_filename, 'wb') as out:
            writer.write(out)
                
if __name__ == '__main__':
    
    for filename in glob.glob('*.pdf'):
        path = filename
        print(path)
        moreSplits = True
        while moreSplits:
            test = input("Filename, min, max?")
            words = test.split(" ")
            if(len(words) == 1):
                moreSplits = False;
            else:
                pdf_splitter(path,words[0], int(words[1]), int(words[2]))
            
    