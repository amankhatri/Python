__author__ = 'kaman'
#difference between class variable and instance variable
class Girl:
    gender = 'female' #a class variable is a variable which will be owned by each object of class girl and will be shared by all objects
    def __init__(self,name):
        self.name = name  #name is going to be unique .
    def print_name(self):
        print(self.name)
sandy = Girl('Sandy')
sally = Girl('Sally')
print(sandy.gender)
#difference between the two statements below is not clear
print(sandy.name)
print((sandy.print_name()))