__author__ = 'Aman'
def dumb_sentence(name = "Bucky", action = "ate", item = "tuna") :
    print("Name: ", name, "Action: ", action, "Item: ",item)
dumb_sentence()
dumb_sentence("How", "Are","you")
#now we have to pass arguments in different order
dumb_sentence(item="Awesomeness")
dumb_sentence(name= "Bee", action= "Autobot")