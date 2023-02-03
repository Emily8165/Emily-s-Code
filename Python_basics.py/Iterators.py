#Iterators:
#An iterator contains a countable number of values.
#This means that the fucntion can triverse thorugh all the values. 
#Python has two main methods for this. __iter__() and __next__()
#tuples, lists, dictionatires and sets are all iterable. 
#they are iterable containers which you can get an iterator from. 
#the iter() method is used to get hese iterations. 

mytuple = ("apple", "bannana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#strings are also iterable objects. 

#LOOPING:
#we can also use a for loop as an iteration cuntions. 
for x in mytuple:
    print(x)
    
#CREATING AN ITERATOR:
#creating a iterator involes creating classes. 
#the iter() method acts in a similer way to init() and it always runs back on itself.
#the next() method is the same as iter() but makes you return to the next item in the sequeance. 

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# if we used a for loop for this iteration or didn't use the __next__(). it would go on forever. 
# to stop it we can use StopIteration

class MyNumbers:
    def __iter__(self): #this is defining the starting point
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
