# use a variable to take the input equation
equation = input("Please enter the equation: ")

# Let's check the type of the variable, this is to check if the variable can be used for calculation  
#print("type of the variable equation is ", type(equation))


# read the equation into a list variable
equation_split = str.split(equation)

# pull the numbers into seperate variables 
n1 = float(equation_split[0])
n2 = float(equation_split[2])

# pull the operator into a variable 
opt = equation_split[1]

# check the what is the kind of operator


# What is the difference between single = and double == 
# transfer of value and other is comparision of value  
#chek = (opt == "+")
#print(chek)


# why colon 


# conditional statement to check if the operator is addition 
if (opt == "+"):
    sum = (n1 + n2)
    print((sum))


# conditional statement to check if the operator is substraction 
if (opt == "-"):
    dif = (n1 - n2)
    print((dif))

# conditional statement to check if the operator is multiplication 
if (opt == "*"):
    pro = (n1 * n2)
    print(pro)
      
# conditional statement to check if the operator is division
if (opt == "/"):
    div = (n1 / n2)
    print(div)
    





