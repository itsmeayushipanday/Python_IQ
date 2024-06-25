#https://chatgpt.com/share/415afd9f-1d71-4a08-864d-eaadfe10dbff

# Class definition init constructor
class hello:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

# Creating an object of the class
obj = hello("ayushi", "panday", 22)

# Printing the attributes of the object
print(obj.fname)  
print(obj.lname)
print(obj.age)
#output
#ayushi
#panday
#22

############################ARRAY PRINTING##############################################################

import array

arr = array.array('i', [1,2,3,4,5])
print("array elements:")
for i in arr:
    print(i)

#############################LIST PRINTING###########################################################

list = [1,2,'ayushi']

for i in list:
    print(i)

#############################SLICING########################################################

list = [1,2,3,4,5,6,7,8,9,10]

print(list[1:5:2])

string = ["ayushi", "pandey", "helloworld", "ram", "siya"]
print(string[0::2])

#output [2, 4]
#['ayushi', 'helloworld', 'siya']

################################UNIT TESTING################################

#Why Unit Testing is Important
#Early Bug Detection: Unit tests help detect problems early in the development process, 
#making it easier to fix them before they become more serious.

#Code Quality: They improve code quality by ensuring that each component functions correctly.

#Simplifies Integration: Unit tests verify the correctness of individual components, 
# simplifying the integration process.

#Isolating Issues: As mentioned, if a complex software system breaks, unit tests help 
# isolate the component causing the failure.

#STUDY ABOUT MORE THIS

############################BREAK CONTINUE PASS################################

list = [1,2,3,4,5,6,7,8]

for i in list:
    if i%2 == 0:
        print(f"first even number: {i}")
        break

#output first even number: 2

for i in list:
    if i%2 == 0:
        continue
    print(f"odd number: {i}")

#output odd number: 1
#odd number: 3
#odd number: 5
#odd number: 7

#########PASS###########
def myfn():
    pass
myfn() #NO ERROR

##########GLOBAL VARIABLES #####
x=10
def ayushi():
    print(x)
ayushi()
#output 10

##########PROTECTED VARIABLES #####

class hello():
    def __init__(self):
        self._protected_var = 20
obj = hello()
print(obj._protected_var)
#output 20

