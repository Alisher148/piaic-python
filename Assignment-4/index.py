# Task 1
number = 15  # You can change this number to test different cases

print("Task 1")

# Check if the number is Even or Odd
if number % 2 == 0:
    print(f"\nEven number: {number}")
else:
    print(f"\nOdd number: {number}")

# Check if the number is Positive, Negative, or Zero
if number > 0:
    print(f"\nPositive number: {number}")
elif number == 0:
    print(f"\nZero number: {number}")
else:
    print(f"\nNegative number: {number}")

# Check divisibility by both 2 and 3, either, or neither
if number % 2 == 0 and number % 3 == 0:
    print(f"\nDivisible by both 2 and 3: {number}")
elif number % 2 == 0 or number % 3 == 0:
    print(f"\nDivisible by either 2 or 3: {number}")
else:
    print(f"\nNot divisible by both 2 and 3: {number}")

# Task 2
age = 17
nationality = "Pakistani"

print("\nTask 2")
if age >= 18:
    if nationality == "Pakistani":
        print("\nYou are eligible to vote.")
    else:
        print("\nPlease obtain a valid ID to vote.")
else:
    print("\nYou are In-eligible to vote.")

# Task 3
_age = 20

print("\nTask 3")
if _age >= 0 and _age <= 12:
    print(f"\nChild: {_age}")
elif _age >= 13 and _age <= 19:
    print(f"\nTeenager: {_age}")
elif _age >= 20 and _age <= 59:
    print(f"\nAdult: {_age}")
elif _age >= 60:
    print(f"\nSenior Citizen: {_age}")
else:
    print(f"\nInvalid Age: {_age}")

# Task 4
month = 3
year = 7

print("\nTask 4")
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(f"\n31 days in month {month}")
elif month == 2:
    if year % 4 == 0:
        print(f"\n29 days in month {month}")
    else:
        print(f"\n28 days in month {month}")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f"\n30 days in month {month}")
else:
    print(f"\nInvalid Month: {month}")
