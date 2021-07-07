# abstract. 

![SCS Flow](https://user-images.githubusercontent.com/63919494/117139606-59564580-ada4-11eb-9de8-125923daa191.png)

## This repository consists of several esoteric scripts for use in the scheme 

`plaint text` -> `salt` -> `nn alg applied` -> `indent (PI)` --[transmit]-- `indent reversed` -> `nn alg applied`
- Conceptual PI replication is feasible for smaller messages, ergo salt. 
- Adversarial derivation of linear (nonstochastic) PI is possible.


Conversion script has no dependancies outside of ciphertext input: converts to binary (utf-8), replaces 1>i & 0>o and then separates each byte with a random string of lowercase letters. The length of this string is between 1 and 10 characters and is decided randomly.
pageindent.py has some prerequisites outlined in datescript.py which is to be implemented locally by SCS client. [libraries & conversions](https://blog.finxter.com/python-convert-unicode-to-bytes-ascii-utf-8-raw-string/)



