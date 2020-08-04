'''
This will scan documents in a dir for a string contained within its document title
Picuture Perfect 2020
'''

import os
from pathlib import Path
import re
import PyPDF4
import pdfminer3
import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

#basic info
folderPath = r"C:\Users\wloeffler\Downloads\11 Sample PDF split_Utility2_Output"
#charsToRemove =['1','2','3','4','5','6','7','8','9','0']
filepathDirs = ['1816','2840','5585','12900','43076', '115066','146208','161649','166591','839624','1000139']


def capitalizeFirstLetterofAllWords(stringInput):
    return ' '.join(elem.capitalize() for elem in stringInput.split())



#taxed from stackoverflow
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    text = retstr.getvalue()
    retstr.close()
    return text







for filefolder in filepathDirs:

    # gets the local file name
    fileNames = os.listdir(folderPath + '\\' + filefolder)
    #gets the full file path
    fullFilePath = [os.path.join(folderPath +'\\' + filefolder+ '\\', x) for x in fileNames]
    #print(str(fullFilePath))

    #the stripper ;)
    strippedFileNames = list()
    for file in fileNames:
        temp = Path(file).with_suffix("")
        temp = str(temp)
        temp = temp.split("_")

        #accounts for non dated ones
        if '-' not in temp[-1]:
            info1 = "Section : "+ temp[1].lower()
            info1 = capitalizeFirstLetterofAllWords(info1)
            strippedFileNames.append(info1)

        #for non dated ones
        else:
            encounterInfo = temp[-2] +': '+ temp[-1]
            encounterInfo = encounterInfo.replace('-','/')
            encounterInfo = capitalizeFirstLetterofAllWords(encounterInfo)
            strippedFileNames.append(encounterInfo)


    #pdf checker part
    for x in range(0,strippedFileNames.__len__()):

        pdfObject = PyPDF4.PdfFileReader(str(fullFilePath[x]))
        stringToSearchFor = strippedFileNames[x]
        #searches each page for the string
        text = convert_pdf_to_txt(fullFilePath[x])
        for y in range(0,strippedFileNames.__len__()):
            if strippedFileNames[y] in text and strippedFileNames[y] != stringToSearchFor:
                print("error in file " + strippedFileNames[x] + "\n it contains "+ strippedFileNames[y])
    print(filefolder)
