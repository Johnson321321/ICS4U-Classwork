from typing import List 


def insert_at(list_input: list, 
            target_value: int, 
            target_index: int) -> List:
    
    return list_input(:target_index + target_value + )
    
    new_list = [0] * (len(list_input) + 1)

    # copy to index
    i = 0
    while i < target_index:
        new_list[i] = list_input[i]
        i += 1

    # insert value at index
    new_list[i] = target_value
    i += 1

    # copy from target to the end
    while i < len(new_list):
        new_list[i] = list_input(i - 1)
        i += 1

    return new_list

def insert_at_2(orginal: list, target_value: int) -> List:
    i = orginal[i] > target_value:

    while i < len(orginal):
        if original[i] > target_value
        