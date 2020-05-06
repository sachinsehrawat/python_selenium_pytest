#raise Exception -Stop the whole code and raise error
'''a= 5
b = 6
print("before execption")
raise Exception("Stop the exection")
print("After Execution")'''

#assert - If true then ok else stop exection
'''a = 5
print("Before assert")
assert(a == 5)
print("After assert")


print("Before assert 2")
assert(a == 6)
print("After assert 2")'''


#try - except - finally
#If try code failes then only execpt will be executed
try:
    a = 5
    sachin()
except:
    print('There is some error in the code')

#print exact error code in exception
try:
    number()
except Exception as e:
    print(e)
    
#finally code will be always exeuted 
try:
    check()
    print("try code here")
except Exception as e:
    print(e)
    print("exception code here")
finally:
    print("Final code here")
    

    
