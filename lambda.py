double=lambda x:x*2
print(double(100))

#instead of writing lengthy code using lambda function you can write lengthy code in two-three lines.#

cube=lambda x:x*x*x
print(cube(5))

number=lambda x:x>10
print(number(88))

#with using multiple value #

avg=lambda x,y:(x+y)/2
print(avg(3,0))

#with using function #

def appl(fx,value):
    return 6+ fx (value)
print(appl(cube,2))
          #fx(function)
          #2,value

