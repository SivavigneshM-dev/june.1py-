# name = input("Enter Your Name")
# print(name.upper())

# from datetime import datetime

# while True:
#     dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
#     try:
#         date_of_birth = datetime.strptime(dob_str, "%Y-%m-%d")
#         print(f"Your date of birth is: {date_of_birth.strftime('%Y-%m-%d')}")
#         break 
#     except ValueError:
#         print("Invalid date format. Please use YYYY-MM-DD.")

# def assign_name_date_of_birth(name,date_of_birth):
#     sum("%y","%d"):
name = input("Enter Your Name")
def generate_password(name, dob):
    

    name = name.lower().replace(" ", "")
    day, month, year = map(int, dob.split("-"))

    password = name[:3].upper()

    password += str(sum(int(digit) for digit in str(day) + str(month)))
    
    password += str(year % 100)[::-1]

    vowels = "aeiou"
    password += str(sum(1 for char in name if char in vowels))

    return password

print(generate_password)

