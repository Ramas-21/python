# -> [start:stop:step]
website1 = "http://google.com"
website2 = "http://w3schools.com"
#-> 7 is the start
# -> -4 is the negative index starting from the right
slice = slice(7,-4)



print(website1[slice])
print(website2[slice])