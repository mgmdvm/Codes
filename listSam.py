import json
import os
import numpy as np


#Open json file with conditions and ratings
with open('conditions.json') as disability:
    data = json.load(disability)

#Create a list of the values from the json dictionary    
myList = data.values()
print(myList)

#Sort the list in descending order 
list2 = sorted(myList, reverse=True)
print(list2)

#convert list to numpy array
newList = np.array(list2)
print(newList)

#convert integers to floats
newList = newList.astype(np.float32)
print(newList)

