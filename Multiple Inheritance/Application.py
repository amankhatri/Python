__author__ = 'kaman'
class Mario() :
    def move(self):
        print("I am moving")
class Shroom():
    def eat_shroom(self):
        print("Now I am big")
class Big_Mario(Mario,Shroom):
    pass #handling syntax but it does nothing smilar to nop this can be used for making class with no functions

bm = Big_Mario()
bm.move()
bm.eat_shroom()
