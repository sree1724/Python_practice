# Input date
day = int(input("Enter day (DD): "))
month = int(input("Enter month (MM): "))
year = int(input("Enter year (YYYY): "))


# Adjust month and year for Zeller's formula
if month < 3:
    month += 12
    year -= 1

# Zeller's Congruence formula
K = year % 100
J = year // 100

h = (day + 13*(month + 1)//5 + K + K//4 + J//4 + 5*J) % 7

# Map result to day name
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(f"The day of the week is {days[h]}.")