# This code is learning about loops 
# 

# Define a list variable with name and age 
age_number = ["Vanshi", 41, "Richa", 41, "Ishaan", 8, "Poorav", 13, "Avi", 10.5]
age_number1 = [ 41, 40,  8,  13,  10]

print(age_number)
# this statement will print the the complete list horizontally and vertical is better in reading. 
# now how do we do that 

print("       ")
print("Name", "\t", "Age")
print("________________________________")
print(age_number[0], "\t" ,age_number[1])
print(age_number[2], "\t" ,age_number[3])
print(age_number[4], "\t" ,age_number[5])
print(age_number[6], "\t" ,age_number[7])
print(age_number[8], "\t" ,age_number[9])
print("________________________________")
print("       ")


# Strings for tab and next line 
# "\t" 


# Now lets use loops to make this code shorter 

# SYNTAX FOR LOOPS 
# for <variablename> in <first to lastnumber list > :


# what is the function range 
# it create a range of value or number from 0 or 1 
print(len(age_number))

print("       ")
print("Name", "\t", "Age")
print("________________________________")

for index in range(len(age_number)):
    print(age_number[index], "\t")

print("________________________________")
print("       ")
