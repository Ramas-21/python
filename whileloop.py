# while loop -> it is a statement that will execute its block of code as long as its condition remain true
name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)