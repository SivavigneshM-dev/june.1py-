
# Odd or even Ascii values 
while True:
    user_input1 = input("Enter a string only: ")

    if user_input1.isdigit():   
        print("Numbers  not Allowed  X ")
        break
    else:
        print(user_input1)
    
    ascii_values = [ord(ch) for ch in user_input1]
    print("ASCII values:",ascii_values)

    odd_values = []
    even_values = []
    
    for asci in ascii_values:
        if asci % 2 != 0:
            odd_values.append(asci)
        else:
            even_values.append(asci)
        
    option = input("ODD or EVEN? ").strip().lower()
    if option == "odd":
        print("ODD ASCII values:", odd_values)
    elif option == "even":
        print("EVEN ASCII values:", even_values)
    else:
        print("Please enter 'ODD' or 'EVEN' only!")



# String & ASCII:

while True:
    user_input2 = input("Enter a string only: ")

    if user_input2.isdigit():   
        print("Numbers  not Allowed  X ")
        break
    else:
        print(user_input2)

    ascii_values = [ord(ch) for ch in user_input2]
    print(ascii_values)

    prime = []
    Non_prime = []

    for asci in ascii_values:
        conut = 0
        for a in range(1, asci + 1):
            if asci % a == 0:
                conut += 1 
        if conut == 2:
            prime.append(asci)
        else:
            Non_prime.append(asci)
    print("Prime values :",prime)
    print("NON-Prime values :",Non_prime)


# String Manipulation & Lists

while True:
    user_input3 = input("Enter letters only  :")
    
    isnumber = False 

    for num in user_input3:
        if num >= '0' and num <='9':
            isnumber = True
            break
    if isnumber:
        print("Numbers Not Allowed  X")
        break
    else:
        print(user_input3)
    
    print("Input string  = :",user_input3)
    print("Reversed_string  =",user_input3[::-1])

    vowels = ["a","e","i","o","u"]

    v = []
    c =[]

    given = user_input3.strip()
    check = given.lower()
    
    for ltr in check:
        if ltr in vowels:
            v.append(ltr)
        else:
            c.append(ltr)
    print("Vowels",v)
    print("Consonants",c)



# Character Filtering    

    
while True:
    user_input4 = input("Enter Text   only (numbers X)  :")

    number_init  = False

    for num in user_input4:
        if num <= '0' or num <= '9':
            number_init = True
    if number_init :
        break
    else:
        print("Working .....")
    

    upper = user_input4.upper()
    print(upper)
    lower = user_input4.lower()
    print(lower)

    choice =  input("What you want ;  Upper or Lower   :")
    choosen = choice.lower()
    if choosen == 'upper':
        print(upper)
    elif choosen == 'lower':
        print(lower)
    else:
        print("Enter the vlaid Option !!")



# ASCII & Sum Operation


while True:
    user_input5 = input("Enter Letters only (Numbers X): ")
    
    isnumber = False 
    for num in user_input5:
        if '0' <= num <= '9':
            isnumber = True
            break

    if isnumber:
        print("Numbers Not Allowed X")
        break

    ascii_values = [ord(ch) for ch in user_input5]
    print(ascii_values)

    odd = []
    even = []

    for val in ascii_values:
        if val % 2 == 0:
            even.append(val)
        else:
            odd.append(val)

    print("Odd :", odd)
    print("Even  :", even)

    total_odd = 0
    total_even = 0

    for num in odd:
        total_odd += num

    for num in even:
        total_even += num

    select = input("Which sum do you want? Odd sum or Even sum?: ")
    answer = select.lower()

    if answer == 'odd sum' or answer == 'oddsum':
        print("Total Odd :", total_odd)
    elif answer == 'even sum' or answer == 'evensum':
        print("Total Even :", total_even)
    else:
        print("Invalid !")

        

        

while True:
    user_input6 = input("Enter Text only    (number  X)         : ")
    
    isnumber = False 
    for num in user_input6:
        if '0' <= num <= '9':
            isnumber = True
            break

    if isnumber:
        print("Numbers Not Allowed X")
        break
    else:
        print("Nice.....")
 
    
    repeated_letters = []
    once_letters = []

    for ch in user_input6 :
        if user_input6.count(ch) > 1 :
            if ch not in repeated_letters:
                repeated_letters.append(ch)
        else:
            if ch not in once_letters:
                once_letters.append(ch)
    
    opinion = input("What do you want? (single or multi) time repeated? ").lower()
    
    if opinion == 'single':
        print(once_letters)
    elif opinion == 'multi':
        print(repeated_letters)
    else:
        print("Input the valid  ('single' or 'multi' !!)")