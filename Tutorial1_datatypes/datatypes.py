# There are four different types of data types 
# 1) str : string are just text 
# 2) Int : Integer are number or integers
# 3) float : Float are decimals
# 4) bool : bool is logic which can TRUE or FALSE

comment= ("Poorav's age is 12")
poorav_age = 12
ishaan_age = 7
print(poorav_age)
print(ishaan_age)
# sum = poorav_age + ishaan_age
# print(sum)
# print(type(sum))
Checkpoint = (ishaan_age > poorav_age)
if(Checkpoint == True):
    print("ishaan is older to poorav")
if(Checkpoint == False):
    print("ishaan is younger to poorav")
    
print(type(Checkpoint))