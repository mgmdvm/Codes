import json
import os
import string
import operator


#Open json file with conditions and percentage ratings
with open('conditions.json') as disability:
    data = json.load(disability)
    
#print(data)
#print(len(data))
