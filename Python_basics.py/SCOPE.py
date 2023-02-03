#The scope referes to the region that a veriable exists in. 
#the scope of the variable x only applies to the func1 so func2 need to be inside it. 
def func1():
    x = 300
    print(x)
    def func2():
        print(x)
    func2()
func1()

#Global variables are variables that effect the whole prgramme. 
#if you redefine the x locally then it will print it out differently locally. 

x = 300

def fun():
    x = 200
    print(x) # will be 200
fun()
print(x) # will be 300

#if you dont want to define a veriable before a fucntion starts, use can use global. 
def myfunc():
    global x
    x = 300
    
myfunc()
print(x)


