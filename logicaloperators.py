# logical operators = (and,or) = used to check if two or more conditional statements is true
temp = float(input("What is the temperature outside? "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today.")
elif temp < 0 or temp >30:
    print("The temperature is bad today.")