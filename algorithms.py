



def add_numbers(numbers_list):
    """
    Ex. add_numbers([9, 5, 11, 6, 1, 15]) returns 47
    :param numbers: a list of numbers
    :return: the sum of all the numbers in the list
    """
    a = 0
    for i in numbers_list:
        a += i
    return a
sample_list = [9, 5, 11, 6, 1, 18]
result = add_numbers(sample_list)
print(result)

def get_max(numbers_list):
    """
    Ex. get_max([45, 23, 99, 34, 67, 98, 0]) returns 99
    :param numbers: a list of numbers
    :return: The largest number in the list
    """
    for i in range(len(numbers_list)-1):
        numbers_list.remove(min(numbers_list[0], numbers_list[1]))
    a = numbers_list[0]
    return a


sample_list = [9, 5, 11, 20, 1, 18]
result_2 = get_max(sample_list)
print(result_2)