import datetime
#ipython pdb
import time
print(time.time())
#strings
my_name = "Sandy Strong"
#stip(), strips away the free space
print(my_name)
print(my_name.capitalize())
#finds how many times does the character occurs.
print(my_name.count('aa'))
#split , splits a string
var = 'my words here'
print(var.split())
var2 = var.split('o')
print(var2)
#finding stuff in string
print(var.find('words'))
#strings are iterables like var[0]
#.startswith returns true or false.
print(var.startswith('my'))
#you can pass variables into strings to format them in a specific way, for example
#similar to c
age = 28
name = 'Sandy'
print("Hello, my name is %s. " %name)
print("Hello my name is %s, and I am %s years old. " %(name, age))

#strip: strps leading or trailing whitespace
#upper: makes all characters upper case
#lower: makes all characters lower case
#split: splits strings into list, whitespace delimited
#find: search for a string within your string
#startswith: test for what your string starts with
#you can pass variables into strings to format them in a specific way, for example
#similar to c


