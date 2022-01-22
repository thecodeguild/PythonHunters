# Few datatypes can be converted 

age_number = ["Vanshika", 41, "Richa", 40,"Ishaan", 7,"Poorav", 11, "Avi", 10.5, "23.8", "23"]

# check the datatype of last value of index
print(type(age_number[10]))

# How do we convert a string datatype to a interger or float datatype
# we will take the list value in a variable 

x10 = age_number[10]
print(x10)
print(type(x10))

# Convert Str to Float
x10_int = float(x10)
print(type(x10_int))
print(x10_int) 

# incase a number inside a string value is having decimals you have to use the command float()
# incase a number inside a string value is having noit having decimals you have to use the command int()


x11 = age_number[11]
print(x11)
print(type(x11))

# Convert Str to Int
x11_int = int(x11)
print(type(x11_int))
print(x11_int) 