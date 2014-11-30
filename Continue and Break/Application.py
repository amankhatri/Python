__author__ = 'Aman'

magicNumber = 26
for n in range(101) :
    if n is magicNumber :
        print("Magic Number is" ,n)
        break # it stops the for loop, that is because when we find magicNumber we stop looping
    else :
        print(n)
#when ever we want to print out numbers with strings instead of print("Bucky" +9) we need to do this:
print("Printing Number", magicNumber)
numbersTaken = [2,5,12,33,17]
print("Here are the numbers that are still available")
for n in range(1,20) : #this will loop through 1 to 19
    if n in numbersTaken :
        continue
    print(n)