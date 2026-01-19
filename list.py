l=[3,5,6]
print(l)
print(type(l))      #printing its type #

      #0,1,2#
marks=[3,5,6]

print(marks)
print(type(marks))
print(marks[0])
print(marks[2])



#negative indexing #

#         -5      -4    -3       -2      -1              #
colors=["red","green","blue","yellow","green"]

print(colors[-1])
print(colors[-3])


#example#
#       012345          #
marks1=[3,5,6,]

print(marks1[-3])     #negative index#
print(marks1[len(marks)-3]) #positive index#
print(marks1[5-3])#5 is the number of marks with including commas #
print(marks1[2])

#check weather item is present in the list or not #

m=[3,5,6,"harry"]

if 7 in marks:
    print("yes")

else:
    print("no")

    if "arry"in "harry":
        print("yes")


        #if you want to print all marks then use #

        print(m)
        print(m[:])

        # list comprehension #

        lst=[i*i for i in range (4)]
        print(lst)

        lst1=[i for i in range(10) if i<=5]
        print(lst1)                          # it will only print number from 0-5 as per condition i have given #