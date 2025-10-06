"""


# Factorial  calculation 

fac = int(input(" number    :"))

fact = 1


for i in range (1,fac+1):
    fact = fact*i
print(fact)



# Prime Number check :

pn = int(input("   number    :"))

if pn % 2 != 0 :
    print("This is prime number ")
else:
    print("Not a Prime Number")



# sum Digits 
sd = input("  Sum of digits   :")

arr = []
sums = 0 
total = 0
for i in sd :
    arr.append(i)
    sums += 1
    for j in range(sums):
        total += 1
print(total)



# remove duplicates form array 

my_arr = input("Enter numbers  with space   :").split()

arr = []
my_tup = ()

result = []

for num in my_arr:
    arr.append(num)
    num.join(my_tup)
    if num not in result:
        result.append(num)
print("With Duplicates ",arr)
print("Without Duplicates ",result)


# revers words  in string 

My_str = input("Enter the text  :")
rever_str = ""

for i in My_str :
    rever_str = i + rever_str
print(rever_str)

"""
"""
# Counting the Length without Using .len() function

user_input  = input("Enter Text ")

length  = 0
my_arr = []

for l in user_input:
    my_arr.append(l)
    length += 1
    if l == " ":
        my_arr.remove(l)
        length -= 1
        
print(length)


"""

# user_input  = input("Enter Text ")

# arr = []
# length = 0

# while True:
#     arr.append(user_input)
#     length += 1
#     if " " in arr:
#         arr.remove(" ")
#         length -= 1
#     print(length)

