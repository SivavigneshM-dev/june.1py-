
"""

# Level of Problem solving 

# 1. Take a list of numbers and return the sum of even numbers only.

My_list  = [1,2,4,5,7,3,12,17,14]

even = 0
ev = []
odd = []

for i in My_list:
    if i % 2 == 0:
        even += i
        ev.append(i)
    else:
        odd.append(i)
print(even)

# 2.Take a string input and count the number of vowels.

c = ""
v = ""
vowel_count = 0
vowels = "aeiou"

name = input("Name  :").lower()
for i in name:
    if i in vowels:
        v += i
        vowel_count += 1
    else:
        c += i       
print(vowel_count)


# 3. Reverse a string without using built-in reverse methods

text = "Tamil Nadu"

length = 0

for i in text:
    length += 1
    
for l in range(length -1,-1,-1):
    print(text[l],end="")



# 4. find the maximum number in a list without using max().

numbers = [3, 7, 1, 9, 4, 8]

mx = numbers[0]

for num in numbers:
    if num > mx:
        mx = num

print(mx)


# 5. Remove Duplicates while maintaining Order
num = [1, 4, 5, 6, 7, 4, 5, 6, 2, 3]
result = []
for n in num:
    if n not in result:
        result.append(n)
for i in range(len(result)):
    for j in range(i + 1, len(result)):
        if result[j] < result[i]:
            result[i], result[j] = result[j], result[i]
print(result)

# 6. Check if a string is a palindrome
text = input("Enter a string: ").lower()
rev = ""
for t in text:
    rev = t + rev
if text == rev:
    print("Palindrome.")
else:
    print("Not a Palindrome.")


    
# 7. Take a list of numbers and move all zeros to the end.
ex_list = [2,4,5,0,2,5,0,1,3,0]
result = []
zero = []

for z in ex_list:
    if z == 0:
        zero.append(z)
    else:
        result.append(z)
    res_list  = result + zero
print(res_list)


"""
#8.  Find the first non-repeating character in a string.


my_name = "siva vignesh"

same  = ""
diff = " "

