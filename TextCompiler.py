
import os
from re import search




f = open("testFile1.txt","a")

AllFiles = os.listdir()
StrTxt = ".txt"
for TxtFile in AllFiles:
    if TxtFile.__contains__(StrTxt):
        print ("Hello")
        fileObject = open(TxtFile,"r")
        data = fileObject.read()
        f.write(data)
        fileObject.close()

f.close()








