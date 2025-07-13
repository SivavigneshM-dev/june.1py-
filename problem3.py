my_list = str(input("ENter Your Name "))
counts = {}

for item in my_list:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

for key, value in counts.items():
    print(f"{key}: {value}")
    
    