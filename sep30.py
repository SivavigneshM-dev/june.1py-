"""



#2.palindrome 

string = input("Text :")
pl = ""
for w in string:
    pl = w + pl
if (string == pl ):
    print("This is Palindrome ")
else:
    print("This is Not a Palindrome ")


#3. Swap tow numbers 
a = int(input("Number 1 :"))
b = int(input("Number 2 :"))
a,b = b,a

print("A :",a," ","B :",b)

#4. Find the largest number 

lrg = input("Number with space  :").split()
My_list = []
for n in lrg :
    My_list.append(n)
    My_list.sort()
print(My_list[-1])

# 5. Find smallest number 
sml = input("Number with space    ").split()
his_list  = []
for m in sml:
    his_list.append(m)
    his_list.sort()
print(his_list[0])

# 6. Counting Vowels & Consonants
v = []
c =[]
Vowels = ["a","e","i","o","u"]
word = input("Enter text  :").strip().lower()
My_arr = []
for x in word:
    My_arr.append(x)
    if x in Vowels:
        v.append(x)
    else:
        c.append(x)
print(len(v))
print(len(c))

#7. Fibanocci series 
a = 0
b = 1
series =  int(input("Series  upto > ?  :"))

print(" ",a," " ,b,end=" ")
for i in range(series):
    c = a + b
    a = b
    b = c 
    print(" ",c,end=" ") 


# 8. Factorial 
fact = 1
num =int(input("Number  :"))
for f  in range(1,num+1):
    fact = fact * f
print(fact)


#10. prime number check 
count = 0
target = int(input("Enter number :"))
for i in range(1,target+1):
    if target % i == 0:
        count += 1
if count == 2:
    print("Prime Number")

else:
    print("Not Prime number ")


# 12.Reverse  words in string 
sentence = input("Enter the sentence gap between words   :").split()
for word in sentence :
    print(word[::-1])



# 13 . Find Even and odd numbers 

Odd = []
Even = []

arr = int(input("Enter array :"))
for i in range(1,arr+1):
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)

print(Odd)
print(Even)


# 14.Array reversal 
My_List = []
num = (input("Enter number :")).strip()
for i in num:
    My_List.append(i)
print(My_List)
print("Reversed",My_List[::-1])


# 15. string Length without Len()

count = 0
str = input("Enter the word  :")
for i in str:
    count += 1
print(count)


# 16. Checking Array sorted 
number = input("Enter numbers  :").strip()
My_arr = []
lnt = len(My_arr)
for c in number:
    My_arr.append(c)
    for j in range(1,lnt+1):
        pass


# 23. Check two strings are anagaram 

My_st1 = []
My_st2 = []

str1 = input("Text1 :").lower()
str2 = input("Text2 :").lower()


for i,j in str1,str2:
    My_st1.append(i)
    My_st2.append(j)

Sort1 = My_st1.sort()
Sort2 = My_st2.sort()

if Sort1 == Sort2:
    print("Anagram ")
else:
    print("Not Anagram ")



#1. Reverse A string 

count = 0
name = input("Text  :")
for i in name:
    count +=1
    length = count
for j in range(1,length+1):
    print()


"""
