import random

def pseudo_list_generator():
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
    The_list = pseudo_list_generator()
    res = search_max_und_min(The_list)
    print(res[0],res[1])


