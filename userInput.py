name = input("What is your name? ")
age = int(input("How old are you? ")) # int() or float() casting the users input (age)
height = float(input("How tall are you? "))

age = age + 1

print("Hello " +name)
print("You are now "+str(age)+" years old")
print("Your height is: "+str(height)+"M")