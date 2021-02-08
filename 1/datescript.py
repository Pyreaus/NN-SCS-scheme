
from random import randint

position = 0
negative_key = {} #referencable positive/negative lists 
positive_key = {}
negative = [] 
positive = []

while position = 0:
  for x in range(1, 366): #set list of pages for 365 days
    negative.append(randint(1, 206)) #(410/2)+1=206 downward
    positive.append(randint(1, 206)) #range upward
  for x in range(1, 366):
    negative_key[x] = negative[x-1] 
    positive_key[x] = positive[x-1]
while position = 1:
  for x in range(1, 366): 
    negative.append(randint(1, 17)) #(32/2)+1=17 downward
    positive.append(randint(1, 17)) 
  for x in range(1, 366):
    negative_key[x] = negative[x-1] 
    positive_key[x] = positive[x-1]
while position = 2:
  for x in range(1, 366): 
    negative.append(randint(1, 3)) 
    positive.append(randint(1, 3)) 
  for x in range(1, 366):
    negative_key[x] = negative[x-1] 
    positive_key[x] = positive[x-1]
while position = 3:
  for x in range(1, 366): 
    negative.append(randint(1, 2)) 
    positive.append(randint(1, 2)) 
  for x in range(1, 366):
    negative_key[x] = negative[x-1] 
    positive_key[x] = positive[x-1]



