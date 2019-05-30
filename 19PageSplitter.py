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
        pdf_splitter(path,"MTG", 0, 6)
        pdf_splitter(path,"Note", 6,10)
        pdf_splitter(path,"RTC", 10,12)
        pdf_splitter(path,"PP", 12,15)
        pdf_splitter(path,"Demo", 15,16)
        pdf_splitter(path,"App", 16,18)
        pdf_splitter(path,"INS", 18,19)
    