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








