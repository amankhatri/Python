__author__ = 'Aman'
#any amount of arguments in function
def add_number(*args): #we dont know how many arguments we are taking , however just store them
    total = 0
    for number in args:
        total = total+number
    return  total
print("The total is: ", add_number(1,2,2))
