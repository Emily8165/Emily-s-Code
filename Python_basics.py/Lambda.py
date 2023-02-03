#Lambada functions:
#lambda are like small anonimous functions. 
#lambda can take alot of argujents but only one can have an expression. 
# the argument is the value given to the fucntion when it is called. 

x = lambda a : a + 10 #the A is the argument to which +10 is being assigned. 
print(x(5))

x = lambda a, b : a * b #this allows you to mulitply and argument by an argument. 
#where a is 5 and b is 6
print(x(5, 6))

#lambda are mainly used inside funtions to add to their purpose. 
def myfunc(n): #so here the argument is n
    return lambda a : a * n # here the lambda is aying the argument a is mulitply by argument n
mydoubler = myfunc(2) # the n is the argument in this func.

print(mydoubler(11)) # this is taking the lambda fucniton of a


