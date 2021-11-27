#We import some of the libraries we need for the program
import csv
import os
import re
import nltk
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

#We will split the text processing with these 3 functions

#This functioon will split the sentences in the paragraph
def fun1():
    with open('united.txt', 'r') as text:
            with open('output.csv', 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                #We make a placeholder cluster column to make the formatting easier
                header = ['sentence', 'cluster']
                csvwriter.writerow(header)
                #We take the line from the txt file
                read = text.readlines()
                for x in read:
                    #We check if the length is big enough to be considered a paragraph
                    if (len(x) > 150):
                        #We split the sentences based on the end punctutation
                        sentenceList = x.split('.')
                        for y in sentenceList:
                            tup2 = (y, 0)
                            csvwriter.writerow(tup2)
                        continue
                    #We use a tuple to store and inser the data
                    tup = (x, 0)
                    csvwriter.writerow(tup)

#This function will remove empty spaces and newline characters
def fun2():
    array = []
    with open('output.csv', 'r', newline='') as csvfile2:
        #We establish a dictionary holding the categories read from the file.
        csv_dict = csv.DictReader(csvfile2)
        #We go through each row and format the text field.
        for row in csv_dict:
            temp = row['sentence']
            #We remove the newline characters
            new = temp.replace('\n', "")
            #We check that the sentence itself is not empty or a newline character
            if temp != "\n" and temp != "":
                array.append({'sentence' : new, 'cluster': row['cluster']})
            #We open the new file we will write our results on.
    with open('outputnew.csv', 'w', newline = '') as youtube_original3_csv:
        fieldnames = ['sentence', 'cluster']
        #We make a dictionary writer to use for the new file.
        csv_writer = csv.writer(youtube_original3_csv)
        #We write the header with the categories on the solution file.
        csv_writer.writerow(fieldnames)
        #We write the final results into the new file using our solution array.
        for row in array:
            csv_writer.writerow((row['sentence'], row['cluster']))

#This function removes the stopwords,weird spaces and specific document formatting chars from the sentences
def fun3():
    #We get the stopwords (english) into an array
    array = []
    stops = stopwords.words('english')
    #We open the file to read and extract the data.
    with open ('outputnew.csv', 'r') as youtube_original_csv:
        #We establish a dictionary holding the categories read from the file.
        csv_dict = csv.DictReader(youtube_original_csv)
        #We go through each row and format the text field.
        for row in csv_dict:
            temp = row['sentence']
            #We remove weird document char
            new2= temp.replace('\ufeff', '')
            #We make the words lowercase
            new6 = new2.lower()
            temparr = []
            temparr.append(new6)
            new3 = ' '.join(temparr).split()
            #We make sure there are no empty values
            new4 = [i for i in new3 if i]
            #If the sentence does not contain anything remove it
            if len(new4) == 0:
                continue
            #We remove the stopwords
            for y in stops:
                if y in new4:
                    new4.remove(y)
            new5 = ""
            #We unite the sentences without the stopwords
            for x in new4:
                new5 = new5 + " " + x
            #We add the formatted text field to the solution array.
            array.append({'sentence' : new5, 'cluster': row['cluster']})
            #We open the new file we will write our results on.
        with open('outputnewnew.csv', 'w', newline = '') as youtube_original3_csv:
            fieldnames = ['sentence', 'cluster']
            #We make a dictionary writer to use for the new file.
            csv_writer = csv.writer(youtube_original3_csv)
            #We write the header with the categories on the solution file.
            csv_writer.writerow(fieldnames)
            #We write the final results into the new file using our solution array.
            for row in array:
                csv_writer.writerow((row['sentence'], row['cluster']))

#We define function to lemmatize each word with its POS tag
def pos_tagger(sentence):
    sent = TextBlob(sentence)
    tag_dict = {"J": 'a', "N": 'n', "V": 'v', "R": 'r'}
    words_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]
    lemma_list = [wd.lemmatize(tag) for wd, tag in words_tags]
    return lemma_list

#This function will lemmatize the sentences
def fun4():
    array = []
    wnl = WordNetLemmatizer()
    with open ('outputnewnew.csv', 'r') as youtube_original_csv:
        #We establish a dictionary holding the categories read from the file.
        csv_dict = csv.DictReader(youtube_original_csv)
        #We go through each row and lemmatize the text field
        for row in csv_dict:
            temp = row['sentence']
            #We lemmatize each word in the sentence
            lemma_list = pos_tagger(temp)
            #We concatenate the lemmatized words
            lemmatized_sentence = " ".join(lemma_list)
            array.append({'sentence' : lemmatized_sentence, 'cluster': row['cluster']})
        with open('outputnewnewnew.csv', 'w', newline = '') as final_file:
            fieldnames = ['sentence', 'cluster']
            #We make a dictionary writer to use for the new file.
            csv_writer = csv.writer(final_file)
            #We write the header with the categories on the solution file.
            csv_writer.writerow(fieldnames)
            #We write the final results into the new file using our solution array.
            for row in array:
                csv_writer.writerow((row['sentence'], row['cluster']))

def fun5():
    array = []
    with open('outputnewnewnew.csv', 'r', newline='') as csvfile2:
        #We establish a dictionary holding the categories read from the file.
        csv_dict = csv.DictReader(csvfile2)
        #We go through each row and format the text field.
        for row in csv_dict:
            temp = row['sentence']
            #We check that the sentence itself is not empty or a newline character
            if len(temp) == 0 or len(temp) == 1:
                continue
            temp = temp.replace('the', '')
            temp = temp.replace('of', '')
            temp = temp.replace('to', '')
            temp = temp.replace('or', '')
            temp = temp.replace('cr', '')
            array.append({'sentence' : temp, 'cluster': row['cluster']})
            #We open the new file we will write our results on.
    with open('final.csv', 'w', newline = '') as youtube_original3_csv:
        fieldnames = ['sentence', 'cluster']
        #We make a dictionary writer to use for the new file.
        csv_writer = csv.writer(youtube_original3_csv)
        #We write the header with the categories on the solution file.
        csv_writer.writerow(fieldnames)
        #We write the final results into the new file using our solution array.
        for row in array:
            csv_writer.writerow((row['sentence'], row['cluster']))


#We call all of the functions in thew right order to execute the preprocessing
fun1()
fun2()
fun3()
fun4()
fun5()

#We delete the files we created along the way to get the finasl result
os.remove("output.csv")
os.remove("outputnew.csv")
os.remove("outputnewnew.csv")
os.remove("outputnewnewnew.csv")

#Maybe remove weird symbols like slaches or certaun puctuations



import re
#We define the function for the Optimal Replacement Algorithm.
def optimal():
    #Establish array of physical memory with the fixed size specified by the user.
    size = 10
    page_faults = 0
    phys_mem = []

    #Read the file
    with open('example_file.txt') as f:
        lines = f.readlines()

    #Filter new line characters from the file just in case and establish the virtual memory array.
    virtual_mem = []
    for x in lines:
        temp = x
        if "\n" in x:
             temp = x.replace('\n', '')
        virtual_mem.append(temp)

    counter = 0
    for x in virtual_mem:
        r = re.search(r'[0-9]+', x)
        temp = ""
        range = r.span()
        for f in x[range[0]:range[1]]:
            temp += f
        virtual_mem[counter] = int(temp)
        counter += 1
    #print(virtual_mem)


    for idx, x in enumerate(virtual_mem):
        if x in phys_mem:
            continue
        else:
            page_faults += 1
            if (len(phys_mem) < size):
                phys_mem.append(x)
            else:
                count_arr = [0] * len(phys_mem)
                #In the double for loop is the edge case of the end referenced number
                for idy, y in enumerate(phys_mem):
                    for idi, i in enumerate(virtual_mem[idx+1:-1]):
                        if i == y:
                            count_arr[idy] = idi
                            break
                    if count_arr[idy] == 0:
                        count_arr[idy] = len(virtual_mem[idx+1:-1]) + 1
                #print(count_arr)
                minim = count_arr.index(max(count_arr))
                phys_mem[minim] = x
    #print(phys_mem)
    return page_faults
