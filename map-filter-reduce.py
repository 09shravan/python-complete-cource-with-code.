l = [1, 2, 4, 6, 8]

def cube(x):
    return x ** 3                      # map()

newl = list(map(cube, l))
print(newl)


#filter(): only the element which will qualify will remain in the list..

o=[3,6,9,12,18]

def filter_function(a):
    return a>10
newnewo=list(filter(filter_function,o))
print(newnewo)

# eg:



foods = ['pancake', 'beckan', 'scrumbel-eggs', 'salad']

def starts_with_s(item):
    return item.startswith('p')

filtered = list(filter(starts_with_s, foods))
print("Here is your menu starting with letter 's':")
print(filtered)

# reduce: #

from functools import reduce

numbers=[1,2,3,4,5]

def mysum(x,y):
    return x+y
sum=reduce(mysum,numbers)
print(sum)