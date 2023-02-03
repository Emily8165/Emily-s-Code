"""This is a file to record what each type of loop does"""
"""WHILE LOOPS"""
"""whilst something is inside the loop the loop will continue
to iterate the loop. Be careful as this is how you can accidently create an infinate loop. 
If th x -= 1 or x += 1 were not in the formula, then 
the loop would go on forever. """
x = 3 # counts down
while x > 0:
    x -= 1
    print(x)
    
i = 1 # counts up 
while i < 3:
    print(i)
    i += 1
    
"""a break is used to stop a while loop early on. This
can break you out of alot of other code though. So be 
careful"""

s = 1 
while s < 6:
    print(s)
    if (i == 5): 
        break
    s += 1
    
"""CONTINUE allows you to edit out certain things from a loop. 
bascailly like sayng if you find this, just ignore it and carry on.
IT IS NOT A CARRY ON FUNCTION"""
i = 0 
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
"""Else allows you add text at teh end of a while loop. 
You can think of a while loop a bit like an if statment 
that just keep repeating and chacking istelf. 
"""
"""FOR LOOPS"""

#For loops are used to iterate through a sequence. 
fruits = ["apple", "bannana", "cherry"]
for x in fruits:
    print(x)

#break is used to break out of a loop so stop the thing basically.
for x in fruits:
    print(x)
    if x == "banana":
        break #this will stop other code coming after it. 

#we can use the continue statment to skip over certain parts of a list. 
for x in fruits:
    print(x)
    if x == "bannana":
        continue
    print(x)

#we can use forloops to iterate thorugh a specific range as wlel. 
for x in range(6):
    print(x)

#if we want to get specific numbers from a range you can set a peramiter in ragne.
for x in range(2, 6):
    print(x)

#for counting up and down:
for x in range(2, 30, 2):
    print(x)

#we can also put else after a for loop to define a pice of code that can be execulted after the for loop is finihsed. 
for x in range(6):
    print(x)
else:
    print("done")

#you can also put loops inside of loops:
#this will print all the x's onto all of the y's
adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)

#we can use the pass statement to avoid getting an error and basically cancles the loop out. 
for x in [0, 1, 2]:
    pass

    