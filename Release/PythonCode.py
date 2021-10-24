import re
import string

#funtion to print frquency of all items
def PrintFrequency():
    counter_dict = {} #creates dictionary
    items = open('Items.txt').read().splitlines() #opens text and creates variable for split lines
 
    #adds item into dictionary and counts frequency
    for word in items:
        if word not in counter_dict:
            counter_dict[word] = 0
            counter_dict[word] += 1 

    #prints dictionary
    for key, value in counter_dict.items():
        print("{}: {}".format(key,value))

#function to search for specific item in text
def PrintSpecific(userString):
    counter_dict = {} #creates dictionary
    items = open('Items.txt').read().splitlines() #opens text and creates variable for split lines
 
    #adds item into dictionary and counts frequency
    for word in items:
        if word not in counter_dict:
            counter_dict[word] = 0
        counter_dict[word] += 1 

    #checks if userString is in dictionary, and outputs that item and frequency
    if userString in counter_dict.keys():
        for key, value in counter_dict.items():
            if key == userString:
                print("{}: {}".format(key,value))
    else:
       print ("That item wasn't purchased today!")
    
    return 0

#function to print histogram  
def PrintHistogram():
    counter_dict = {} #creates dictionary
    items = open('Items.txt').read().splitlines() #opens text and creates variable for split lines
 
    #adds item into dictionary and counts frequency
    for word in items:
        if word not in counter_dict:
            counter_dict[word] = 0
        counter_dict[word] += 1 
    
    #writes dictionary into new file 
    with open("frequency.dat", 'w') as newFile:
        for key, value in counter_dict.items():
            newFile.write('%s %s\n' % (key,value))
    
    

