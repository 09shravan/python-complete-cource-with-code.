
x = 4
print(x)                #this is outside the function so it will be an global function #
#in simple way they are not destroyed easily #

# creating a function #
def hello():
    x = 5
    print(f"the local x is {x}")    #the local variables are destroyable:it will only execute at once#
    print("hello world")            #what ever value we give inside the the function will be an local function#

print(f"the global x is {x}")
hello()
print(f"the global x is {x}")
print(f"the local x is {x}")  #look at that example #

#another examole#

x=10           #global variable #

def my_function():
    y=1          #local variable #
    print(y)

my_function()
print(x)


#if you want to change x=10 to any other value #

x=10           #global variable #

def my_function():
    global x
    x=4
    y=1          #local variable #
    print(y)

my_function()
print(x)
print(y)