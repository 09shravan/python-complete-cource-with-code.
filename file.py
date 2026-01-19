f=open('excercise','a')
text=f.write('')
print(text)
f.close()

# in this method when ever you go to the excercise file that you have writter ie:
# ('he is a good guy') it will overwites it multiple number of time whenever you acess rhe excercise file..#

f=open('excercise','r')
text=f.read()
print(text) #in this read mode you can ecess that what-ever is in the excercise file written on yourv current
#file compiler #
f.close()

#methods#

f = open('excercise', 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

#in this readline method if your filce contain data which is messy it will help to maintain it clearly #

#another example#
f = open('excercise', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break

    parts = line.strip().split(",")
    if len(parts) >= 3:
        m1 = parts[0]
        m2 = parts[1]
        m3 = parts[2]
     #   print(f"marks of student {i} in math is : {m1}")
      #  print(f"marks of student {i} in science is : {m2}")
       # print(f"marks of student {i} in english is : {m3}")
    #else:
      #  print(f"Line {i} does not have enough data.")

f.close()


#writelines method()#

f = open('excercise', 'w')
#lines = ['line1 \n', 'line2 \n', 'line3 \n']#
#f.writelines(lines)#
f.close()


#seek()#


with open('excercise','r') as f:
    print(type(f))        # Prints the type of the file object
    f.seek(10)            # Moves the file pointer to the 10th byte
    data = f.read(5)      # Reads 5 characters from there
    print(data)           # Prints those 5 characters


#truncate#
with open('excercise', 'w+') as f:
    f.write('hello-world')
    f.truncate(3)
    f.seek(0)
    print(f.read())