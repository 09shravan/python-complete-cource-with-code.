s={2,4,5,6,4}
print(s)                   # it ignore repetable value #

info={"carla",19,5.9,19,'false'}
print(info)                                  # unordered collection #

shravan={}
print(type(shravan))          # if we uses ( shravan={} then the type will be dictionary )#

shravan=set()
print(type(shravan))         # if we uses ( shravan=set() then the type will be set )#

info={"carla",19,5.9,19,'false'}
for value in info:
    print(value)              # the value will be printed as in a line but withour order #


s1={2,4,6,8}
s2={10,12,14,6}
print(s1.union(s2))  # joining two sets together,but not the repetable value#


num={5,10,15,20,25}
num1={30,35,40,10}
num.update(num1)              # just like union set #
print(num)

cities={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
                                             # in this case it will print the data which is in both the sets (common) #
cities3=cities.intersection(cities2)
print(cities3)

cities={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
                                                   # intersection set #
cities.intersection_update(cities2)
print(cities3)

# symmetric difference #

cities={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
                                                   # value which are not common in both the sets #
cities3=cities.symmetric_difference(cities2)
print(cities3)



cities={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}

cities3=cities.symmetric_difference_update(cities2)
print(cities3)


cities={"tokyo","madrid","berlin","delhi"}
cities2={"delhi","seoul","kabul"}

cities3=cities.difference(cities2)           # value which are not common in only one set#
print(cities3)

# isdisjoint #
cities={"tokyo","madrid","berlin","delhi1"}
cities2={"delhi","seoul","kabul"}
                                              # it check if the item of given set is present in another set if its present it will show false else true  #
print(cities.isdisjoint(cities2))

#superset#

cities={"tokyo","madrid","berlin","delhi"}
cities2={"seoul","kabul"}
print(cities.issuperset(cities2))   # it will check if weather seoul and kabul is present in (cities) or not #

#issubset#

cities={"tokyo","madrid","berlin","delhi"}
cities2={"seoul","kabul"}
print(cities.issubset(cities2))

#add#

cities={"tokyo","madrid","berlin","delhi"}
cities.add("kashmir")              #it is use to add the element it can only add one argument at a time #
print(cities)

#remove#

cities={"tokyo","madrid","berlin","delhi"}
cities.remove("delhi")
cities.discard("delhi")
print(cities)

#pop#

cities={"tokyo","madrid","berlin","delhi"}
item=cities.pop()
print(cities)              #it will pop any elements #
print(item)

#check if items exists #

info={"carl",19,5.9,19,'false'}

if "carla" in info:
    print("carla is a good girl")

else:
    print("she is a bitch")