#Create a file and write a list in it
with open('animals.txt', 'w') as writer:
    animals = ['dog', 'cat', 'lion', 'fish', 'chicken']
    for line in animals:
        writer.write(line + '\n')
#with open('animals.txt', 'r') as reader:
    #print(reader.read())
with open('animals.txt') as reader:
        text  = reader.readline()
        sum = 0
        while text != '' :
           print(text)
           text = reader.readline()
           sum = sum + 1
print(sum)
           
           
       
       
