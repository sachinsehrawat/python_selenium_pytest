'''#Declare Varibale in Python
a = 10
b = 'Sachin'
print(b + " is " + str(a))
print("{} is {}".format(b, a))
print(type(b))'''

'''#Data type in Python
age = 27
print(type(age))

distance = 2.5
print(type(distance))

name = "Sachin"
print(type(name))

#List
friends = ['sachin', 'sakshi']
print(type(friends))
num3 = [[1,2,3], [4,5,6], [7,8,9]]
print(num3[1][2])

print(friends[0])

friends.insert(1, 'Sehrawat')
print(friends)
friends[0] = friends[0].upper()
print(friends)
del friends[1]
print(friends)

#tuple
friends2 = ('sachin', 'sakshi')
print(type(friends2))
friends2.append('Sehrawat')'''

#Dictonaries - Key:Value pair
'''dict = {
    'name' : 'Sachin',
    'age' : 15,
    3: 9,
    5: "top",
    }

print(dict)
print(dict['age']) 

dictk = {}

dictk["Name"] = "Sachin"
dictk["Age"] = 27
print(dictk)'''

#If - Else condition
'''a = 5
if a > 3:
    print("A is greater than 3")
else:
    print ("A is smaller than 3")
print("If-else ended")'''

'''a = input("enter a number: ")
if int(a) > 3:
    print("A is greater than 3")
else:
    print ("A is smaller than 3")
print("If-else ended")'''

#For loops

'''for i in range(5):
    print(i)

games  = ['Foootball', 'BasketBall', 'Chess']
for i in games:
    print(i)

for i in range(5,10):
    print(i)

for i in range(10,-1,-2):
    print(i)'''

#While Loops
'''age = 15

while age<20:
    print("Age is: " + str(age))
    age = age+1'''

#Break is loops is used to end the loop
'''for i in range(10):
    if i == 4:
        break
    print(i)'''

#Continue in loops is used to skip the current iternation

'''for i in range(10,15):
    if i == 13:
        continue
    print(i)'''

#Function is python

def add(a,b,c):
    return a+b+c

print(add(1,2,3))






