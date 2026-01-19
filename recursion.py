def factorial(n=5):
    if(n==0 or n==1):
        return 1

    else:
        return n*factorial(n - 1)

print(factorial(5))                    # so basically the factorial is means 5*4*3*2*1=120#


# fibonacci series #

def factorial(n):
    if(n==0 or n==1):
        return 1

    else:
        return n+factorial(n-1)           # just change the sign #

print(factorial(10))
