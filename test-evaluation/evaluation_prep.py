from typing import Dict
from typing import List


def cal_sum(a: int, b: int) -> int:
    ''' add a integer.

    Arge:
        a: an integer 
        b: an integer
    
    Return:
        the sum of the two integers
    '''
    return a + b


def cal_list_sum(num_list: List[int]) -> int:
    '''gives the sum of the list

    Arge:
    num_list: a list of integers

    return:
    the sum of all the =intergers in the list
    '''

    sum = 0
    for i in num_list:
        sum += i
    return sum


def count_occurances(words: List[str]) -> Dict:

    ''' Get occurances of words in a list.
    Args:
    words: A list of words 
        
    Returns :
    dictionary of the number of occurances
    for each words in the list.
    '''

    occurances = {}
    for word in words:
        if word not in occurances.keys():
            occurances[word] = 1
        else:
            occurances[word] += 1
    
    return occurances

