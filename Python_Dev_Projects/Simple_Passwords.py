#Goal is to create a simple password generator. 
#password should be 9 charactures long, contain at least 1 number, contain at least one capital letter, and contain one special charatures. 

import random
import string
from string import punctuation

lowerletters = string.ascii_lowercase
 ranlow = random.sample(lowerletters, k=3)
listlow = list(ranlow)
upperletters = string.ascii_uppercase
         ranhi = random.sample(upperletters, k=3)
listhi = list(ranhi)
numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
ranum = random.sample(numbers, k = 1)
listnumb = list(ranum)
spc = set(punctuation)
ranspc = random.sample(spc, k = 1)
spc1 = list(spc)
password = ranhi + ranlow + ranspc + ranum
listp = list(password)
ranpass = random.sample(listp, k = 8)
print("here is your new randomised password: ")
print(''.join(ranpass))
