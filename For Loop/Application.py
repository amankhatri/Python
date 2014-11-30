__author__ = 'Aman'
food = ["Bacon", "Tuna", "Ham", "Sausages", "Beef"]
for f in food : #f is place holder so for each item f in food
    print(f)
    print(len(f))
    print("In the loop")
print("out of the loop")
for f in food[:2] :  #start at the begning and stop at Tuna
    print(f)