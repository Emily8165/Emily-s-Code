#CLASSES 
#Classes are used like a blueprint for storing funcations. 
#This is how to create a class
class Myclass:
    x = 5
y = Myclass
print(y.x)

#We can use the __init__() function to create an object and add properites to it. 
#Here we are give charicturatistics to the age and name objects and then calling them. 

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

x = person("Emily", 23)
print(x.name)
print(x.age)

#The __str__() function control the object if it is a String. 
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} {self.age}" #here we also use an F string to make sure we can take the obejcts inputs. 
# if you try to run this code without the str then it will just return itself.
x = person("Emily", 23)
print(x)

#Object methods are fucntions that belong to an object. 
#So this allows you to store data in an object 
#and then call that object with a functions. 
#have a look below
class person:
    def __init__(self, name, age): #the self parameter referes to the first instance in the fucntion in the class. 
        self.name = name #both self's marry up. 
        self.age = age
        
    def func(self):
        print("Hello, my name is " + self.name)

x = person("Emily", 23)
x.func()

#modifying an object. 
x.age = 40 
del x.age
del x
#its that easy

#Pass stagement, Classes cannot be empty so use the pass stagement to avoice and error. 
class person:
    pass

#INHERITANCE
#This allows some classes to inherit other classes into them. 
#Parent class is the class that is passing on the objects it is also called the base class. 
#Child class is the class that is inheriting objects form anohter class, it is also called a derived class. 
#PARENT CLASS
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
x = person("Jon", "Doe")
x.printname()
#CHILD CLASS - just set the parent class as a peramiter
class student(person):
    pass

x = student("mike", "olsen")
x.printname()

#adding in a __init__()Function
#This goes in instead of the pass key word. 
# when this happens the child class does not inherit the parents fucntion and overides it. 
# but you can use this to add to the parents objects as well. 
#for example:
class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)
#this keep the inheriance funtion and lets us add fucntios to the child one. 

#SUPER FUCNTION
#the super fucntion makes the child class inherit all objects from the parent class. 
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        #this just makes it easier as you don't have to name the parent. 

#ADDING PROPERTIES:
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year # this allows you to add another object in. 
        
x = student("mike", "olsen", 2019)
print(x)

#Adding methods
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year 
    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)




