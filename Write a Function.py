
# Write a function about whether it is a leap year or not

def is_leap(year):
    leap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return leap
        else:
            return True
    else:
        return leap


print("Welcome! This program will hep you identify whether your birthday was on a leap year or not")
year = int(input("Please enter the year you were born in: "))
print(is_leap())