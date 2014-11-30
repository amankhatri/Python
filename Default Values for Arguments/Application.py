__author__ = 'Aman'
def get_gender(sex='Unknown'): #default value of sex is Unknown
    if sex is "m" :
        sex = "Male"
    elif sex is "f" :
        sex = "Female"
    else :
        sex = "Unknown"
    print("Sex",sex)
get_gender('m')
get_gender()
get_gender("f")
