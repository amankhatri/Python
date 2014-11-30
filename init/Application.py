__author__ = 'kaman'
class Tuna :
    def __init__(self): #this is something similar to initialization, so when ever you make an object of class this will be executed
        #you can conclude that _init_ is a constructor
        print("Initialization function")
    def swim(self):
        print("Tuna Swiming")

tuna1 = Tuna()
tuna1.swim()
print('New Class')
class Enemy:
    def __init__(self,x):
        self.energy = x
    def get_energy(self):
        print(self.energy)
jason = Enemy(10)
jason.get_energy()
sandy = Enemy(20)
sandy.get_energy()