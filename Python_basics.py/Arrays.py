#ARRAYS
#an array is a way of storing multiple values in one sinle variable. 

cars = ["ford", "volvo", "BMW"]

#an array is a special variable that can hold more then one value ata  time. 
# an array allows you to cycle through a number of variables and indexes ahead of tiem. 
x = cars[0] # selects a specific item in the array.
print(x)

cars[0] = "Toyota" #this iwll replace the first psoitin in an array
print(cars)

x = len(cars) # used to find the length of the array
print(x)

cars.append("honda") #will add honda into the array and iwll be put on the end. 

cars.pop(1) #will allow you to pop out an elent in the array.

cars.remove("BMW") # will remove any value that has BMW in it. 

for x in cars: #allows you to iterate the whole array
    print(x)





    