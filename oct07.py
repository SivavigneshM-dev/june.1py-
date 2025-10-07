
# Today going to work with while Loop ✌️

print("1 to  10 ")

i = 1
while(i <= 10 ):
    print("Loop no :",i,"is running")
    i += 1

# While loop Questions 

print("Print the numbers  Reverse ")

n  = 10 

while (n > 0):
    print(n)
    n -= 1

# Sum
print("Sum First N numbers ")

num = 10 

sum = 0 

i = 1 
while i <= num:
    sum += i 
    i += 1
    print(i)
print(sum)



# Even Numbers 
num = 1
even = 0
while num <= 20:
    if num % 2 == 0:
        even += 1
        print(num)
    num += 1


# Multiplication table 5

i = 1
t = 5

while i <= 10:
    print(i,"X",t,"=",i*t)
    i += 1

# Level 2 :-   Input Based 
# user  Input Sum  until 0 

total = 0

while True :
    i = float(input("Numbers if '0 stop' "))
    if i == 0:
        break
    total += i
print(total)



# Password checker 
password = input("Enter the New password  :")
retry = 0

while True:
    i = input("Enter the correct password !  :")
    if i == password:
        break
    retry += 1
print("ACCESS GARNTED ")

# Positive Numbers only 

i = 0 
while True:
    n = int(input("+ve Number   :"))
    if n < 0 :
        break
    i += 1
print("OOPs You Entered -ve Value ")

# Guess the Number 

k = 0 
while True :
    u = int(input("No  1-10  H or L '0 to stop '  :"))
    if u > 5:
        print("High")
    elif u < 5:
        print("Low")
    elif u == 5 or u == 0:
        break
    else:
        print("Number between 1 to 10 !")
        
    k += 1



# Calculate the factorial 

n = int(input("Factorial Calc: "))
fact = 1
i = n

while i > 0:
    fact *= i
    i -= 1

print(fact)


# Level 3 :- String Manipulation 

# Reverse String
s = input("Text: ")
text = ""
i = len(s) - 1

while i >= 0:
    text += s[i]
    i -= 1
print(text)

# Remove spaces
text = input("Text: ")
result = ""
i = 0

while i < len(text):
    if text[i] != " ":
        result += text[i]
    i += 1

print(result)


# Conut Vowels 
vowels = "aeiou"
count = 0
u = input("text")
i = len(u)-1
while i >= 0:
    if u[i].lower()in vowels:
        count += 1
    i -= 1
print(count)

# Count digits in a string
text = input("Number  :")
count = 0
i = 0
while i < len(text):
    if text[i].isdigit():
        count += 1
    i += 1

print(count)
