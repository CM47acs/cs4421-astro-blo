# testing
import random


day = random.randint(1,8)

if day > 4.1:
    cat = True
else:
    cat = False
if cat: 
    cat_status = "meow"
else:
    cat_status = ""
print(cat_status)

if cat:
     dog_status = "bark"
else: 
     dog_status = "ZZZ"
print(dog_status)