#PY MATCH
training = 4
match training:
  case 1 :
    print("First Class")
  case 2 :
    print("Second Class")
  case 3 :
    print("Third Class")
  case 4 :
    print("Fourth Class")
  case 5 :
    print("Fifth Class")
  case 6 :
    print("Sixth Class")

# _____________________

#_ Value 
month = 2
match month :
  case 10 :
    print("October")
  case 11 :
    print("November")
  case 12 :
    print("December")
  case _ :
    print("Looking for the New Year")

# _____________________

# Combine Values | 1 | 2 | 3 |
time  =  6
match time :
  case    7 | 8 :
    print("Preparing to Going School  ") 
  case 9 | 10 | 11  :
    print("Study Time  ")
  case 12 | 1 :
    print("Lunch Time ")
  case 2 | 3 | 4 :
    print("After Noon Class  ")
  case 5 | 6   :
    print("Tution Time ")
# _____________________
# if statment as Gaurds
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")