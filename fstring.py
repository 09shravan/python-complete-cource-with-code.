letter="hey my name is {} and i am from {} "

country="india"
name="shravan"

print(letter.format (name,country))
print(letter.format (country,name))

# by adding number also #

letter1="hey my name is {0} and i am from {1} "

country="india"
name="shravan"
                 #     0  ,  1     #
print(letter.format (country,name))

# with the help of using fstring #

print(f"hey my name is {name} and i am from {country}")

# whith the help of using 2f #

# Correct way to use format()
txt = "for only {price:.2f} dollars !"
print(txt.format(price=49.9999))

# with f string #
rupees = 49.9999
txt1 = f"for only {rupees:.2f} dollars !"
print(txt1)

# you can evaluate a string #

print(f"{2*30}")
print(type(f"{2*30}"))