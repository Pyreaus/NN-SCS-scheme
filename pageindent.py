from datetime import datetime
import datescript
import string
from itertools import combinations_with_replacement

class Indent: #p-h-w-s-v
  def __init__(self, p, v, s, w, h):
    self.p = p
    self.v = v # each layer is reversably set
    self.s = s  
    self.w = w
    self.h = h

  def h_shuffle(self): #instantiate under
    if len(datescript.random_hex[datescript.random_list[datetime.now().timetuple().tm_yday]]) < 3260: 
      try: 
        self.h = datescript.random_hex[datescript.random_list[datetime.now().timetuple().tm_yday]]] 
      except: 
        pass 
    else: 
      try: #reset current indent
        self.h -= datescript.positive_key[datetime.now().timetuple().tm_yday] 
      except:
        return False     

  def p_shuffle(self):
    if (self.p + datescript.postive_key[datetime.now().timetuple().tm_yday]) <= 410: #current date formatted as x/365 valule
      datescript.position = 1
      try: #set variables to match new indent
        self.p += datescript.negative_key[datetime.now().timetuple().tm_yday] 
      except: 
        pass #proceed to try positive key
    else: 
      try: #reset current indent
        self.p -= datescript.positive_key[datetime.now().timetuple().tm_yday]
      except:
        return False #overlap

  def v_shuffle(self):
    if (self.v + datescript.postive_key[datetime.now().timetuple().tm_yday]) <= 32:
      datescript.position = 2
      try: #reset current indent with negative key
        self.v += datescript.negative_key[datetime.now().timetuple().tm_yday] 
      except: 
        pass #proceed to try positive key
    else: 
      try: #reset current indent with positive key
        self.v -= datescript.positive_key[datetime.now().timetuple().tm_yday] 
      except:
        return False 
    
  def s_shuffle(self):
    if (self.s + datescript.postive_key[datetime.now().timetuple().tm_yday]) <= 5:
      datescript.position = 3
      try: #reset current indent with negative key
        self.s += datescript.negative_key[datetime.now().timetuple().tm_yday] 
      except: 
        pass #proceed to try positive key
    else: 
      try: #reset current indent with positive key
        self.s -= datescript.positive_key[datetime.now().timetuple().tm_yday] 
      except:
        return False 

  def w_shuffle(self):
    if (self.w + datescript.postive_key[datetime.now().timetuple().tm_yday]) <= 4:
      datescript.position = 4
      try: #reset current indent with negative key
        self.w += datescript.negative_key[datetime.now().timetuple().tm_yday] 
      except: 
        pass #proceed to try positive key
    else: 
      try: #reset current indent with positive key
        self.w -= datescript.positive_key[datetime.now().timetuple().tm_yday] 
      except:
        return False 
