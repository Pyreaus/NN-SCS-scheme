from itertools import combinations_with_replacement
import string
import random

position = 0
negative_key = {} #referencable positive/negative lists 
positive_key = {}
random_hex = {}
random_list = []

while position == 0:
  for x in range(1, 366): #set list of pages for 365 days
    negative_key[x] = random.randint(1, 206) #(410/2)+1=206 downward
    positive_key[x] = random.randint(1, 206) #range upward
while position == 1: 
  for x in range(1, 366):
    negative_key[x] = random.randint(1,17) #(32/2)+1=17 downward
    positive_key[x] = random.randint(1,17)
while position == 2:
  for x in range(1, 366):
    negative_key[x] = random.randint(1, 3)
    positive_key[x] = random.randint(1, 3)
while position == 3:
  for x in range(1, 366):
    negative_key[x] = random.randint(1, 2)
    positive_key[x] = random.randint(1, 2)   
    
sequence = [string.ascii_letters.lowercase(), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
comb = combinations_with_replacement(sequence, 3260)
list = [' '. join(x) for x in sequence if x < 3260]
for x in range(1, 366):
  random_hex[x] = random.choice(list)
for x in range(1, 366):
  random_list.append(random.randint(1, 1631)    



