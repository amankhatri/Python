__author__ = 'kaman'
#inheritance
class Parent():
    def print_last_name(self):
        print("Roberts")
class Child(Parent):  #empty parenthesis are used to type in the name of the parent class
    def print_first_name(self):
        print("Bucky")
#a child can override the function in parent class method
    def print_last_name(self):
        print("last Name ")
c = Child()
c.print_first_name()
c.print_last_name()
