__author__ = 'Aman'
def health_calculator(age,apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate*3.5) - (cigs_smoked*2)
    print(answer)
health_calculator(24,7,0)
buckys_data = [27,20,0]
health_calculator(buckys_data[0],buckys_data[1],buckys_data[2])
#if there are tons of people we need to use list
health_calculator(*buckys_data) # this is unpacking list so it unpacks bucky_data and do this health_calculator(buckys_data[0],buckys_data[1],buckys_data[2])
