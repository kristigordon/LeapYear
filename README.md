### LeapYear

This project calcualates whether a year is a Leap Year or not and the logic was pretty interesting. 

This is how you work out whether if a particular year is a leap year.
```
Every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
```
**For example:**

The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

```
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
```

In this code, I wanted to be able to see step by step where something was failing so that I was able to ensure that each piece of logic was working properly. 

The "trick" of this problem was looking at the if statements.
Originally, I put % 4 == 0 first, however if this condition passes, then the program does not run the elif statements. 

So instead, I needed to concatonate % 4 == 0 and % 100 == 0 into one test followed by % 4 == 0 and % 400 == 0 to ensure that we were ruling out the chance that something wasn't a leap year first. 

Then I had the % 4 == 0 statement followed by an else = Not a Leap Year to cover every year that wouldn't fall into one of these first 3 categories. 

This was a fun little project that got me thinking about if statements a little more strategically. 
