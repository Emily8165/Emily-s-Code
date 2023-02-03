#DATETIME

import datetime

x = datetime.datetime.now()#used to print the time now. 
print(x)

#creating date objects. 
#Datetime() is a class that we can use to construct the date
x = datetime.datetime(2020, 5, 17) #you need a minimum of three arguments to create the date. 
print(x)

#strtime()is used" to return one part of the current date

print(x.strftime("%B")) # it will output the date as a string. 
