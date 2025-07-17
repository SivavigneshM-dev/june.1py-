# Add two numbers 
print("SUM")

a = int(input("Input the 1st number  :"))
b = int(input("Input the 2nd number :"))

sum = a+b
print(sum)

# multiply 
print("MULTI")
x = int(input("Input the 1st number  :"))
y = int(input("Input the 2nd number :"))

multi = x*y
print(multi)


#division 
print("DIV")
q = int(input("Input the 1st number  :"))
r = int(input("Input the 2nd number :"))

div = q/r
print(div)


# Swap two numbers

print("SWAP")

numb = input("Enter two separate numbers with a comma: ")

numb_split = numb.split(",")

a = int(numb_split[0])
b = int(numb_split[1])

a, b = b, a

print(a , b)


#print the text with spaced letters

print("SPACE")
word = input("Enter hello world  ")

words_space = ' '.join(word)

print(words_space)

#odd numbers

print("ODD or EVEN numbers ")

odd_or_even = int(input("Enter any number"))

if odd_or_even % 2 == 0 :
    print("Even Number")
else :
    print("Odd Number")


#loop
print("Loop")
i = 1
nubr = int(input("Enter any number  : "))
while i <= nubr:
    print(i)
    i = i + 1

   

#print even numbers 
print("Now printing even numbers by loop !!!")

e = 2
even = int(input("enter any even number  : "))
while e <= even:
    print(e,end=",")
    e = e + 2


#Odd numbers 
print("Now printing odd numbers  by loop !!!")

o = 1
odd = int(input("Enter any odd number  :"))
while o<=odd :
    print(o,end=",")
    o += 2

# Calculate product

print("Product ")

numbers = input("Enter two numbers separated by '/': ")

num1, num2 = map(int, numbers.split('/'))

product = num1 * num2

print(product)


# pattern 
print("Pattern")
rows = int(input("Enter the Number for the pattern: "))
for i in range(1, rows + 1):  
    for j in range(rows  - i):  
        print(" ", end=" ")
    for k in range(1, 2 * i):  
        print("*", end=" ")
    print()

#print list 
print("print the list !!")
tup = tuple(input("enter five numbers : "))

li = list(tup)

print(li)

# Average
print("Average")
avg = input("Enter three numbers 'with (,)':  ")
numbr = [int(num.strip()) for num in avg.split(',')]

total = sum(numbr)
average = total / len(numbr)

print(average)


#Assending order 
print("Assending order")

num = input("Enter the numbers: ")        
digits = list(num)                       
digits.sort()                            
sorted_num = ''.join(digits)              
print(sorted_num)


#Descending order
print("Descending order")

no = input("Enter the numbers: ")        
digit = list(no)                        
digit.sort(reverse=True)          
sort_no = ''.join(digit)              
print(sort_no)

#only odd numbers 

print("Only odd numbers ")
on= input("Enter multiple numbers separated by spaces: ").split()

odd_number = []

for n in on:
    if int(n) % 2 != 0:
        odd_number.append(int(n))

print(odd_number)


#only Even  numbers 

print("Only Even  numbers ")

en= input("Enter multiple numbers separated by spaces: ").split()

eve_number = []

for n in en:
    if int(n) % 2 == 0:
        eve_number.append(int(n))

print(eve_number)


#vowels only 
print("Vowels Only ")
vowel =  input("enter some text ")

vowel_Text = []
check_Txt = ["a","e","i", "o", "u"]

for ch in vowel:
    if ch.lower() in check_Txt:
        vowel_Text.append(ch)

print(vowel_Text)


#vowels count !!!
print("vowel text count")
vowel =  input("enter some text ")

vowel_Text = []
check_Txt = ["a","e","i", "o", "u"]

for cv in vowel:
    if cv.lower() in check_Txt:
        vowel_Text.append(cv)

print(len(vowel_Text))


#list comparision
print("list comparision ")

l1 = list(map(int,input("Enter some numbers with space: ").split()))
l2 = list(map(int,input("Enter some numbers with space: ").split()))
if l1 == l2 :
 print("The list is Equal ")
else:
 print("The list is Not Equal")

#To find positive or Negative 

print("positive or negative number ")

think = int(input("Enter positive or negative number  :"))
if think > 0:
 print("Positive Number")
else :
    print("Negative Number ")

#Array reverse
print("Array reverse")

avg = input("Enter three numbers separated by commas: ")
numbr = [int(num.strip()) for num in avg.split(',')]

numbr.sort(reverse=True)

sort_Avg = ', '.join(str(num) for num in numbr)

print(sort_Avg)

#Largest number in a array 
print("Biggest number in the array ")
array1 = input("Enter numbers with space : ")
arr = array1.split(' ')
arr = [int(x.strip()) for x in arr]  
print(max(arr))



#Smallest number in a array 

print("Smallest number in the array ")
array1 = input("Enter numbers with space : ")
arr = array1.split(' ')
arr = [int(x.strip()) for x in arr]  
print(min(arr))

# Reverse string 

print("Reversing the String ")

string11 = input("Input some letters with space: ")
string11 = string11.lower()  
string2 = string11.split(' ')
string2.reverse()  
print(string2)




