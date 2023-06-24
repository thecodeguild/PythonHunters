# This code is for learning to slice and dice a list

age_number = ["Vanshika", 41, "Richa", 40, "Ishaan", 8, "Poorav", 13, "Avi", 10.5]
age_number1 = [ 41, 40,  8,  13,  10]

print(type(age_number))

age_number_elder = age_number[0:4]

# index always starts with 0 so every number would count -1 
# when we pick a subset by using : it will select index one less than tha number which is given 
# this does not include the last index it include number upto an index 

print((age_number_elder))

age_number_younger = age_number[4:10]

print((age_number_younger))

age_number_rand = age_number[4:8]

print((age_number_rand))

age_number_name = age_number[1:11:2]
# [Start index : last index : skip index ]

print((age_number_name))

# HOW TO CHECK THE LENGTH OF THE LIST 

age_number_len = len(age_number1)

print((age_number_len))





























