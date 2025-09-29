
print("repeated values")  

num_str = input("Enter numbers separated by ',' : ")
my_list = list(map(int, num_str.split(',')))


repeated  = []
my_list.sort()
my_sorted_list = []
for i in my_list:
    my_sorted_list.append(i)
    if my_sorted_list.count(i) > 1 and  i not in repeated:
        repeated.append(i)
print(repeated)


print("Unique Elements Only")

Unique_number = input("Enter numbers separated by ',' : ")
list_unique = list(map(int, Unique_number.split(',')))

list_unique.sort()

unique = []
for i in list_unique:
    if list_unique.count(i) == 1: 
        unique.append(i)

print(unique)



print("Second lagest number")

n = input("Enter numbers separated by ',' : ")
num = list(map(int, n.split(',')))
num.sort()
print(num[-2])


print("Reverse  the each  word")

word = input("Enter a word : ")
print(' '.join(word[::-1] for word in word.split()))



print("Anagram Checker")

a = input("Text  a :")
b = input("Text  b :")

if sorted(a) == sorted(b):
    print("It is Anagram")
else:
    print("Not Anagram ")

    
print("Sum Digits") 


count = 0
n = int(input("Number: "))

for i in str(n):   
    count += int(i)
print(count)


print("second method of Sum Digits")

num = int(input("Number: "))
print("Sum is :",sum(int(d) for d in str(num)))


text = input("Enter a string: ")

for letter in text:
    if text.count(letter) == 1:   
        print("One time text :", letter)
        break
else:
    print("No non-repeated text")



print("Find Common Elements")

l1 = [x.strip() for x in input("Enter list1 (separate by ','): ").split(',')]
l2 = [x.strip() for x in input("Enter list2 (separate by ','): ").split(',')]

common_elements = []
for element in l1:
    if element in l2 and element not in common_elements:
        common_elements.append(element)

print("Common elements:", common_elements)


