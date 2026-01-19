dic={
    "harry":"human being",
    "spoon":"object"
}
print(dic["harry"])      # you are acessing key pairs #

dict={
     344:"shravan",
     342:"yash",
     670:"shraddha",
     355:"priyanka"
}
print(dict[670])

# how you can acess it.. #

info={'name':'shravan','age':'19','cource':'bca'}
print(info)

#if you want to print particular value #

info={'name':'shravan','age':'19','cource':'bca'}
print(info)
print(info['name'])
print(info.get('cource'))

# acessing multiple value #

info={'name':'shravan','age':'19','cource':'bca'}
print(info)
print(info.keys())          # so it will acess name,age,cource.#

for keys in info.keys():
    print(info[keys])       #it will acess value in order #

print(info.values())        #it will acess values like shravan,19,bca etc.#


for key in info.keys():
    print(f"the value corresponding to the key {key} is {info[key]}")

    # acessing key value pairs #

info={'name':'shravan','age':'19','cource':'bca'}
print(info.items())    #it will acess both keys-pairs#


             #  methods in python #

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
                            #it will join two dictionaries  together#
ep1.update(ep2)
print(ep1)


info={'name':'shravan','age':'19','cource':'bca'}
print(info)
info.update({'age':20})       # it will help in  adding or updating dictionary#
info.update({'dob':2005})
print(info)


ep1={122:45,123:89,567:69,670:69}
ep1.clear()                # it will clear the dictionary #
print(ep1)

info={'name':'shravan','age':'19','cource':'bca'}
info.pop("name")           # pop will remove the key values #
print(info)

info={'name':'shravan','age':'19','cource':'bca'}
info.popitem()           # pop will remove the [last] key values #
print(info)

info={'name':'shravan','age':'19','cource':'bca'}
del info['age']         # it will delet the specific  values  #
print(info)