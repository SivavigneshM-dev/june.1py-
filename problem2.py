name = input("Enter Your Name")
print(name.upper())

from datetime import datetime

while True:
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        date_of_birth = datetime.strptime(dob_str, "%Y-%m-%d")
        print(f"Your date of birth is: {date_of_birth.strftime('%Y-%m-%d')}")
        break 
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def assign_name_date_of_birth(name,date_of_birth):
    sum("%y","%d")
    print()
    
