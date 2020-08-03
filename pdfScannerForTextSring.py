'''
This will scan documents in a dir for a string contained within its document title
Picuture Perfect 2020
'''

import os
from pathlib import Path
import re

#basic info
folderPath = r"C:\Users\wloeffler\Downloads\11 Sample PDF split_Utility2_Output\12900"
#charsToRemove =['1','2','3','4','5','6','7','8','9','0']


def capitalizeFirstLetterofAllWords(stringInput):
    return ' '.join(elem.capitalize() for elem in stringInput.split())


#gets the local file name
fileNames = os.listdir(folderPath)

#gets the full file path
fullFilePath = [os.path.abspath(x) for x in fileNames]


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


