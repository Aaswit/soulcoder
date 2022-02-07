#In Python indexing starts from 0
#but we can also have negative index
#which will start from end like -1,-2 etc

#Now lets dive in the world of Python!!


name = "Tony Stark"
print ('T' in name)    #returns true
print("Aashu" in name) #returns false

print (5/2)  #prints 2.5
print (5//2) #prints 2    //removes decimal

print(5 ** 2)  #5 raise to the power 2    #prints 25


age = 2

if age >=18:
    print("You are an adult")#only prints if condition is true
    print("you  can vote")
elif age < 18 and age > 3:
        print("you are in school")
else:
    print("you are a baby")

print("Thank You")    #always print


i = 1            #while loop 
while i<= 5:
    print(i * "*")
    i = i + 1   


for item in range(10):   #forloop
    print(item + 1)   #prints 1-10

#creating a list
marks = [95,98,97]  #any datatype is allowed in lists
for score in marks:
    print(score)

# some experiments on list
marks.append(99)   #append means adding
print(marks)

marks.insert(0, 92)  #92 is added at 0 index
print(99 in marks)   #returns true

marks.clear()  #clears whole list
print(marks)

#break statement
students = ["ram", "shyam", "kishan", "radha", "radhika"]

for student in students:
    if student == "radha":
        break          #comes out of the loop
    print(student)     #prints till kishan 

# [] - list, () - tuple, {} - set 
# set{} dont have an index, therfore we call it unordered

#In-built functions have been used like int(), str()
#module functions
from math import sqrt  #importation
#gives square-root of any no.
print(sqrt(16))

#user-defined functions
def print_sum(first, second):
    print(first + second)
print_sum(1,2)  #gives sum of these two nos.

#Thats all of Python Basics!
# Thanks :)