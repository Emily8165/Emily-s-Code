#CONTACT BOOK
#create a programme that will store the name, age, and location of people. 
#the programme should also allow you to add people to it. 
kev = []

def cb():
    class contactbook:
        def __init__(self, name, age, gender, location ):
            self.name = name
            self.age = age
            self.gender = gender
            self.location = location 
        def __str__(self):
            return f"{self.name} {self.age} {self.gender} {self.location}"
    w = str(input("Give name: "))
    x = int(input("Give age: "))
    y = str(input("Give gender: "))
    z = str(input("Give location: "))
    c = contactbook(w, x, y, z)
    print(c)
    kev.append(c)
    print(kev)
    def end():
        i = input("would you like to add more names to the contact book? y/n: ")
        while i != "n":
            return(cb())
            break
    end()
    print(kev)
cb()

"""
Nyall = contactbook("Nyall", 27, "Male", "Leicester")
Anna = contactbook("Anna", 23, "Female", "leicester")
Alex = contactbook("Alex", 26, "Male", "London")
"""


"""
a = dict("Alex", 26, "male", "clapham")
b = ["Anna", 23, "female", "clapham"]
c = ["Nyall", 27, "male", "Leicester"]
"""

def data():
    global names 
    names = ["alex", "anna", "nyall"]
    global ages
    ages = [26, 23, 27]
    global gender
    gender = ["other", "male", "female"]
    global location
    location = ["clapham", "leiester", "london"]
data()
def append_data():
    a = input("select the data you wish to change about a person: name, age, gender, location, all or append: ")
    def cb():
        global Alex
        Alex = {"name" : "Alex",
                "age" : 21, 
                "gender" : "male", 
                "location" : "Clapham"}
        print(Alex)
        global Anna
        Anna = {"name" : "Anna", 
                "age" : 23, 
                "gender" : "female", 
                "location" : "Guildford"}
        print(Anna)
        global Nyall
        Nyall = {"name" : "Nyall", 
                "age" : 27, 
                "gender" : "Male", 
                "location" : "Leicester"}
        print(Nyall)
    def all():
        f = input("give me a name: ")
        g = input("give me thier age: ")
        h = input("tell me thier gender: ")
        i = input("tell me thier location: ")
        newdict = {"name" : f,
                   "age" : g, 
                   "gender" : h, 
                   "location" : i}
        print(cb())
        print(newdict)# will not allow newdict to be added due to cb() not being able to take positional argument. 
    def append():
        j = input("who's data do you want to append?: ")
        k = input("which data do you want to change, name, age, gender, location?: ")
        l = input("please insert the data you want added: ")
        
        if j == "Alex":
            if k == "name":
                Alex.update("name", l)
            elif k == "age":
                Alex.update("age", l)
            elif k == "gender":
                Alex.update("gender", l)
            elif k == "location":
                Alex.update("location", l)
            else:
                print("that is incorrect, try again: ")
                append()
                
        if j == "Anna":
            if k == "name":
                Anna.update("name", l)
            elif k == "age":
                Anna.update("age", l)
            elif k == "gender":
                Anna.update("gender", l)
            elif k == "location":
                Anna.update("location", l)
            else:
                print("that is incorrect, try again: ")
                append()
        
        if j == "Nyall":
            if k == "name":
                Nyall.update("name", l)
            elif k == "age":
                Nyall.update("age", l)
            elif k == "gender":
                Nyall.update("gender", l)
            elif k == "location":
                Nyall.update("location", l)
            else:
                print("that is incorrect, try again: ")
                append()

    if a == "name":
        b = input("please add the new name: ")
        names.append(b)
    elif a == "age":
        c = int(input("please add and age: "))
        ages.append(c)
    elif a == "gender":
        d = input("please insert new gender: ")
        gender.append(d)
    elif a == "location":
        e = input("input new location: ")
        ages.append(e)
    elif a == "all":
        all()
    elif a == "append":
        append()
    else:
        print("error")
    append_data
    
append_data


