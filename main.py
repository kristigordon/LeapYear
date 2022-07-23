year = int(input("Which year do you want to check?\n"))

#on every year that is evenly divisible by 4
#**except** every year that is evenly divisible by 100
#**unless** the year is also evenly divisible by 400


if (year % 4 == 0) and (year % 100 == 0):
    print("This is not a Leap Year - Condition 1 Failed")
elif (year % 4 == 0) and (year % 400 == 0):
    print("This is not a Leap Year - Condition 2 Failed")
elif year % 4 == 0:
    print("This is a Leap Year! - First 2 conditions failed")

else:
    print("This is not a Leap Year")