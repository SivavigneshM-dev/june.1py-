#   Date
# Get the current date and time
import datetime


now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# List and Tuple

values = input("Input some comma-separated numbers: ")

list = values.split(",")
tuple = tuple(list)

print('List : ', list)


print('Tuple : ', tuple)



# Display the first and last colors from the list
color_list =[ "red", "blue" , "Brown" , "Green" , "Orangre "]
print("First color: ", color_list[0])


# Exam shedule
exam_st_date = (10, 11, 2025)
print("the exam will start from : %i/%i/%i" % exam_st_date)


#Number expansion Calculator 
def expand_number(num):
    num_str = str(num)
    length = len(num_str)
    expanded_parts = []
    
    for i, digit in enumerate(num_str):
        if digit <= '10':
            expanded_parts.append(digit + '10' * (length - i - 1))
    
    return ' + '.join(expanded_parts)
print(expand_number(1234))  # Output: 1000 + 200 + 30 + 4
