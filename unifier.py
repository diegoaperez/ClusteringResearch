#We import the libraries we need
import os
import docx

#To get the files in dir the script and the txt files should be the only thing on the folder
filenames = os.listdir()

#We remove the redundant script name from the list of file names
filenames.remove("unifier.py")
filenames.remove(".DS_Store")
filenames.remove("csv:txt.py")

#print(filenames)

# #We open each file and group all of their text under one file
with open('united.txt', 'w') as outfile:
    for fname in filenames:
        doc = docx.Document(fname)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        for para in text:
            outfile.write(para)
