#date time :-#

import datetime
x=datetime.datetime.now()
print(x)

y=datetime.datetime(2005,8,9)
print(y)                           #you can personalize your own date #

# if we want more info like day,year,month etc........#

import datetime

z = datetime.datetime(2005, 8, 9)
print(z.strftime("%a"))  # a=short form of day
print(z.strftime("%A"))  # A=full form of day
print(z.strftime("%B"))  # B=which month
print(z.strftime("%m"))  # m=which month in numerical form
print(z.strftime("%y"))  # y=last 2 digit of an year
print(z.strftime("%Y"))  # Y=which year
print(z.strftime("%p"))  # p=for am & pm
print(z.strftime("%M"))  # M=for minutes
print(z.strftime("%F"))  # F=for macroseconds

# random module:-#

import random
x=random.randint(1,90)
print(x)                  #randint will help to choose random num (only integer)#

i=['shravan','shradha','tiger','salman']
i=random.choice(i) #if you want random strings then apply first string and with the help of an choice:#
print(i)

#math:-#

import math

x=max(77,12,0)
print(x)

x=min(77,12,0)
print(x)

x=pow(2,5)  #multiply 2 with 5 times 2*2*2*2*2=32#
print(x)

x=math.sqrt(77)
print(x)

x=abs(-77) # converts pos to pos & neg to pos#
print(x)

x=math.ceil(2.1) # it makes 2.1=3,1.1=2#
print(x)

x=math.floor(7.7)
print(x) #it only contain first decimal value #