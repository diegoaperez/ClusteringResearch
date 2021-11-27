#We import the libraries we need
import os
import docx

#To get the files in dir the script and the txt files should be the only thing on the folder
filenames_proto = os.listdir()

#We remove the redundant script name from the list of file names
filenames_proto.remove("unifier.py")
filenames_proto.remove(".DS_Store")
filenames_proto.remove("csv:txt.py")

#We make it s owe can filter which section of the files we want.
filenames = []
for x in filenames_proto:
    if "Course" in x:
        filenames.append(x)

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

#Make a script to make seperate documents for each diffrent part with a csv column of that part.
