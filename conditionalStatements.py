# if statements = a block of code that will execute if its condition is true
age = int(input("How old are you? "))

if age >= 18:
    print("you are an adult.")
elif age == 100:
    print("You are blessed.")
elif age <= 0:
    print("You have not been born yet.")
else:
    print("You are a child.")