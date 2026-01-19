# you cannot change tuple #

tup=(1,5,7)
print(type(tup),tup)

tup=(1)
print(type(tup),tup)    # in bracket if we use (1) then the type will convert into an integer #
tup=(1,)
print(type(tup),tup)    #if we use an (1,) an comma then the type will be tuple only #


tup=(1,4,78,55,4,9,0)     #positive indexing#

print(tup[0])
print(tup[2])
print(tup[3])
print(tup[4])


shravan=(1,2,3,4,5)      # total number are 5 so lengths are also 5 #

print(len(shravan))
print(shravan[5-2])
print(shravan[3])

# slicing #

tup1=tuple[1:4]
print(tup1)

# methods in python #

tuple1=(1,3,4,6,7,9,0,3,3,3,3)
res=tuple1.count(3)  # will show the number of occurence of a given item #
print(res)


res=len(tuple1)
print(res)                  # help in finding the length of an tuple #


