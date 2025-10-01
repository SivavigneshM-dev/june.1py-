"""

my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted array:", my_array)

"""

user_input = input("Enter the country code ")
if user_input == '91' :
    print("you'r selected the India" )
elif user_input == '98':
    print("You'r selected the Iran ")
elif user_input == '55':
    print("you'r selected Brazil")
else:
    print("enter valid '91' ,'98', '55' ")

number = int(input("enter the phone number "))
my_List = []
length = len(my_List)
for i in  number:
    my_List.append(i)
    if length == 10:
        print("India",my_List)
    elif length == 11:
        print("Iran",my_List)
    elif length == 8:
        print("brazil",my_List)
    else:
        print("Invalid   digits !!")
    print("\n""You entered ",user_input," ",my_List )