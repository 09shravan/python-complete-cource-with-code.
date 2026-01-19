try:

    l=[1,5,6,7]
    i=int(input("enter the index:"))
    print(i(i))

except:
    print("some error occured")

finally:
    print("i am finally occured")     #in this keyword (finally) the statement will occurs not matters what in the complier#


    #custom errors#


    a=int(input("enter valve between 5 to 9 : "))

    if(a<5 or a>9):
        raise valueerror("value should be between 5-9")  #you can raise or custom your own errors #