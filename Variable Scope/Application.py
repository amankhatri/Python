__author__ = 'Aman'
a = 1000
def corn() :
    b = 2000
    print(a)
    print(b) # b is only valid in the function corn
def fudge():
    print(a)
corn()
fudge()

