# if else statements 
age = int(input())

if age >= 18 :
    print ("Eligible for voting")
else :
    print("Not Eligible for Voting ")



# _____________________

# while loop

count  = 0 
while (count <= 3 ):
    count = count + 1
    print("Hello vicky brooo..")

# _____________________

# for loop syntax 

n = 5 
for i in range (0, n ):
    print(i)

# _____________________

# Nested loops Syntax 

# from __future__ import print_function
# for i in range (1,5):
#     for j in range(i):
#         print(i, end=' ')
#     print() 

# # _____________________

# break statement

for number in '9235279272':
    if number == '2' or '9' :
        break
print('current number :',number )

# _____________________

# functions
def  evenOdd(x: int) ->str:
    if (x / 2 == 0) :
        return "Even"
    else:
        return "Odd"
print(evenOdd(12))
print(evenOdd(9))

# _____________________


# Positional Arguments
def nameAge(name ,age):
    print("Hi ,I am ",name)
    print("My age is ", age)


print("case-1:")
nameAge("Siva", 21 )


print("\ncase-2:")
nameAge(21 ,"Siva")
