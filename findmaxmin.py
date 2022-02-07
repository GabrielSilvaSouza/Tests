#Since computers are fast calculators - and the problem only demands a list with 100 numbers -
#we can use For Loop to run through the list comparing each number with the first one - not entering in subject such as BINARY SEARCH. If the 
# 'i' in the list is greater(or smaller to minimum value case) than the first value the initial value changes to 'i' 
# and do it again until the last digit.

#But before, we generate a list with 100 random numbers in the range of ten thousand numbers.


import random

def pseudorandom_list_generator():
    random_list = random.sample(range(10000), 100)
    return random_list

def search_max_und_min(array):
    max_value = array[0]
    min_value = array[0]
    for i in array:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    
    return max_value,min_value

        
if __name__ == '__main__':
    The_list = pseudorandom_list_generator()
    res = search_max_und_min(The_list)
    print('Maior valor lido: {} \nMenor valor lido: {}'.format(res[0],res[1]))


