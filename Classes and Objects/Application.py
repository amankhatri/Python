__author__ = 'kaman'
class Enemy :
    life = 3
    def attack(self): #when ever we use self that means use something from the same class that is Enemy class
        print("Ouch")
        self.life -= 1  #accessing class variables
    def checkLife(self):
        if self.life <= 0 :
            print("Dead")
        else:
            print(str(self.life) + " Life Left")
#creating an object for Enemy class
enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()

enemy2 = Enemy()
enemy2.attack()
enemy2.attack()
enemy2.checkLife()