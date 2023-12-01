#Steve
#11.30
#Birthday Paradox

import random
from itertools import combinations
def get_birthdays():
    '''
    get the birthdays of 23 people
    :return: the list of people
    '''
    global a #call a as global
    a = []
    for i in range(23):
        a.append(random.randint(1, 365)) #put 23 random birthdates at the list
    return a

def probablity():
    '''
    get every combination of 23 people, and using for loop, it judge if there is any same birthdate
    :return: True/non
    '''
    b = list(combinations(a, 2)) #get the list of all the combinations of two element in the lists of birthdates.
    for i in b: #judge if there is any pair that has same number.
        if i[0] == i[1]: #for certain element of list, compare two number in that element(element is another list)
            return True


def main():
    '''
    collect datas at list, uses functions above to run the simulations and give results,
    with providing probabilities at the end.
    :return: nothing
    '''
    data = [] #create list to put information about same or different
    while True:
        get_birthdays()
        if probablity() == True: #if there is same two birthdates, print same and append data at the 'data' list
            data.append(1)
            print('same')
        else: #if there is no two same birthdates, print different and append corresponding data at list.
            data.append(0)
            print('different')
        if len(data) == 10000: #finish when run 10000 times
            break
    print(f'probability: {data.count(1)*100/len(data)}%') #print the probability in percentage
main()