__author__ = 'kaman'
while True:
    try:
        number = int(input('What is your favorite number'))
        print(18/number)
        break
    except ValueError :
        print('Make sure and enter a number')
    except ZeroDivisionError :
        print('Dont pick zero')
    except :
        print('This can hide a lot of your problems so please dont use is too much')
    finally:
        print('this part will be definately executed')