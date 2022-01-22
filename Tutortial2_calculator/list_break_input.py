# This code is to read a input command or equation and break it up to different variables using lists. 

# use a variable to take the input equation
equation = input("Please enter the equation: ")

# Let's check the type of the variable, this is to check if the variable can be used for calculation  
print("type of the variable equation is ", type(equation))

# why the data type is str
# variable assigned to an input command is always a string 
# In this form the variable cannot be used for calculation

# How to convert the string to float
#x =float(equation)

#print("type of the variable x is ",type(x))

# We will test this code by giving random inputs as a compbination of numbers and strings 
# test 1 : we will input 25.4
# test 2 : we will input 25.3 + 3
# test 1 will be success 
# test 2 will throw error , value error at line no 14

# How do I break the input string to different values of equation 
# How to convert a string to a list 
# we will take a varible for list and convert the equation variable to list 
equation_lst = str.split(equation)

# lets print and see 
print(equation_lst)
print(type(equation_lst[0]))

# will the list values be in int/float or string , it will be in string and thats why before we do any calculation we have to convert it to float. 

n1 = float(equation_lst[0])
opt = equation_lst[1]
n2 = float(equation_lst[2]) 

# now lets add the numbers  

sum = n1 + n2 

print("Sum of number is ", sum )