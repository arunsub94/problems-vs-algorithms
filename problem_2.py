
def get_pivot(input_list, first_index, last_index):
    """
    A recursive function to get index of element around which array is pivoted.
    Args:
        input_list(array), first_index, last_index: Input array to search and the target along with the fitst and last indices
    Returns:
    int: Index of the element around which array is rotated or -1
    """

    if first_index > last_index:
        return -1

    if first_index == last_index:
        return first_index

    mid = (first_index + last_index)//2

    if (mid < last_index and input_list[mid] > input_list[mid + 1]):
        return mid
    if (first_index < mid and input_list[mid] < input_list[mid - 1]):
        return (mid - 1)
    if (input_list[first_index] >= input_list[mid]):
        return get_pivot(input_list,first_index, mid - 1)
    return get_pivot(input_list, mid + 1, last_index)

def binary_search(search_list, start, end, target):
    """
    Find the index by searching in a sorted array

    Args:
       search_list(array), target(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    while start <= end:

        mid = start + (end - start)//2

        if (search_list[mid] == target):
            return mid
        elif (search_list[mid] < target):
            start = mid + 1
        else:
            end = mid - 1

    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    n = len(input_list)
    pivot_index = get_pivot(input_list, 0, n - 1)

    if(pivot_index == -1):
        return binary_search(input_list, 0, n - 1, number)

    if (input_list[pivot_index] == number):
        return pivot_index

    if (input_list[0] <= number):
        return binary_search(input_list, 0, pivot_index, number)

    return binary_search(input_list, pivot_index + 1, n - 1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

#Edge Case 1
test_list=[i for i in range (1011,10000)]+[i for i in range (0,1011)]
test_function([test_list, 6])
#egde test 3  large list with negative numbers
test_list=[i for i in range (1011,10000)]+[i for i in range (-1000,1011)]
test_function([test_list, -60])
