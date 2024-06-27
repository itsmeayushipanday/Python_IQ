##############LIST COMPREHENSION#############

my_list = [1,2,3,4,5]
new_list = [x**2 for x in my_list]
#print(new_list) [1, 4, 9, 16, 25]

list2 = [x**2 for x in my_list if x%2 != 0]
#print(list2) [1, 9, 25]

list1 = [1,2,3,4]
list3 = [1,2,3,4]
list4 = [(x+y) for (x,y) in zip(list1,list3)] #parallel iterator 
list5 = [(x,y) for x in list1 for y in list3] #nested iterator
#print(list4)  [2, 4, 6, 8]
#print(list5) [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

list6 = [[1, 2, 3], [4, 5, 6], [7,8,9]]
list7 = [x for temp in list6 for x in temp]
#print(list7) [1, 2, 3, 4, 5, 6, 7, 8, 9]

###########DICT COMPRESSION #########

dict1 = {1:1, 2:2}
dict2 = {x:x**2 for x in dict1}
#print(dict2) {1: 1, 2: 4}

dict3 = {x: x**2 for x in dict1 if x%2 == 0}
#print(dict3) {2: 4}

###############DECORATORS #################################
#SIMPLE FUNCTION
#def hello():
#   print('Hello Ayushi')
#hello()

#NOW DECORATOR FUNCTION APPLIES

def lowercase_decorator(function):
    def wrapper():
        func = function()
        if func is not None:
            lower_msg = func.lower()
            return lower_msg
        return None
    return wrapper

def split_decorator(function):
    def wrapper():
        func = function()
        if func is not None:
            split_msg = func.split()
            return split_msg
        return None
    return wrapper

@split_decorator
@lowercase_decorator
def hello():
    return 'Hello Ayushi'
#print(hello()) ['hello', 'ayushi']

def capitalize_decorator(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        hello = function(arg1, arg2)
        return hello
    return wrapper
@capitalize_decorator
def hi(name1, name2):
    return 'Hello' + " " + name1 + " "  + name2
#print(hi('ayushi', 'panday')) Hello Ayushi Panday


x=10 # global variable
def out_fn():
    y=20 #enclosed variable
    def in_fn():
        z=40 #local variable
        #print(x,y,z) 10 20 40
    in_fn()
out_fn()

#########OVERRIDE #########
x=10
def fn():
    x=20
    print(x)
#print(x)
#fn()
#print(x) 
#10
#20
#10

##SOLUTION #########
x=10
def fn():
    global x
    x=20
    print(x)
#print(x)
#fn()
#print(x)
#10
#20
#20


#########LAMBDA FUNCTIONS ######### lambda arguments : expression
#Assigning lambda functions to a variable:  
hello = lambda a,b : a*b
#print(hello(2,2)) 4


#Wrapping lambda functions inside another function:
def fn(n):
    return lambda a : a*n
h1 = fn(2)
#print(h1(5))  10

def square(x):
    return x**2
#print(square(5)) 25

sq_lambda = lambda x : x**2
#print(sq_lambda(5)) 25

map1 = [1,2,3,4,5,6,7,8,9,10]
map_lambda = list(map(lambda x : x**2, map1))
#print(map_lambda) [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

filter1 = [1,2,3,4,5,6,7,8]
filter_lambda = list(filter(lambda x : x%2 == 0, filter1))
#print(filter_lambda) [2, 4, 6, 8]


########DELETE FILE################
#import os
#file_name = "example.txt"
#try:
#   os.remove(file_name)
#    print(f"File '{file_name}' deleted successfully!")
#except OSError as e:
#    print(f"Error deleting '{file_name}': {e.strerror}")


#########args#################

def fn(a, b, *args):
    mul = a*b
    for num in args:
        mul *= num
    return mul
#print(fn(1,2,3,4,5))  120

##########kargs #########

def fn(**kargs):
    for key, value in kargs.items():
        print(key + ": " + value)
#fn(Name = "Ayushi Panday", Like="Music")  
#Name: Ayushi Panday
#Like: Music


###########JOIN AND SPLIT ###########
text = "My name is Ayushi Panday"
word = text.split()
ans = "-".join(word)
#print(word)
#print(ans)
#['My', 'name', 'is', 'Ayushi', 'Panday']
#My-name-is-Ayushi-Panday
        

#################ITERATOR################

list1 = [1,2,3,4,5]
iter_list = iter(list1)
#print(next(iter_list))
#print(next(iter_list))
#1
#2


##########PASS BY VALUE AND PASS BY REFERENCE################################
def fn(arr):
    arr.append(10)
arr = [1,2,3,4,5]
#print(arr)  #pass by value 
#fn(arr)
#print(arr) #pass by reference


#import math
#print(dir(math))


############GENERATORS########

def fib(n):
    p, q = 0, 1
    while(p<n):
        yield p
        p, q = q, p+q

for num in fib(10):
    print(num)

#0
#1
#1
#2
#3
#5
#8


##############SHALLOW COPY##############
import copy
list1 = [1,2,[3,4]]
shallow_copy = copy.copy(list1)
#shallow_copy[2][0] = 10
#print(list1)          [1, 2, [10, 4]]
#print(shallow_copy)      [1, 2, [10, 4]]

#This modifies the nested list [3, 4] within shallow_copy to [10, 4].
#Since both list1 and shallow_copy share the same reference to the nested list [3, 4], 
#any modification made to this nested list through shallow_copy will also affect list1.
#Therefore, list1 is now [1, 2, [10, 4]].



shallow_copy[0] = 50
#print(list1)        [1, 2, [3, 4]]
#print(shallow_copy) [50,2,[3, 4]]
#When you modify shallow_copy[0], you are assigning a new integer object (50) to that 
#position in shallow_copy. list1 still retains the original integer 1 in its first position.



list2 = [1,2,[3,4]]
deep_copy = copy.deepcopy(list2)

deep_copy[2][0] = 10

#print(list2)   [1, 2, [3, 4]]
#print(deep_copy)     [1, 2, [10, 4]]

#shallow me nested objects ki copy nahi bnti..isliye shallow-copy me change krne se 
#original me bhi change
#but deep copy me nested objects ki copy bnti hain..toh deep_copy me chnage krne se 
#original me change nahi hoga