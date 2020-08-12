def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr_sorted = merge_sort(left_arr)
    right_arr_sorted = merge_sort(right_arr)

    return merge(left_arr_sorted, right_arr_sorted)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while (left_index < len(left) and right_index < len(right)):

        if (left[left_index] <= right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #Referencing the assumption that input list only has array elements ranging from 0 to 9,
    #any inputs larger than this, will consequently raise a ValueError.
    try:
        #handling single inputs
        if (len(input_list) < 2):
            raise ValueError
        #handling very large numbers
        for  el in input_list:
            if (el > 9):
                raise ValueError
    except ValueError:
        print("Input list should have atleast two numbers in the range from 0 to 9. Try again!")
        return False

    input_len = len(input_list)
    sorted_list = merge_sort(input_list)
    print(sorted_list)
    if input_len % 2 == 0:

        first_num = 0
        second_num = 0

        num_digits = input_len//2

        for i in range(num_digits):
            first_num += (10**i) * sorted_list.pop(0)
            second_num += (10**i) * sorted_list.pop(0)

    else:

        first_num = 0
        second_num = 0

        num_digits = input_len//2

        for i in range(num_digits):
            first_num += (10**i) * sorted_list.pop(0)
            second_num += (10**i) * sorted_list.pop(0)

        first_num += (10**(i+1)) * sorted_list.pop(0)

    return [first_num, second_num]

    pass

def test_function(test_case):

    output = rearrange_digits(test_case[0])
    if (output):
        solution = test_case[1]
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case = [[0,0,1,1,2],[210, 10]]
test_function(test_case)

#edge case 1
test_case = [[0,0],[0,0]]
test_function(test_case)

#edge case 2: large set and large numbers
test_function([[i for i in range(0,21)], [int("".join(map(str,range(20,-1,-2)))), int("".join(map(str,range(19,-1,-2))))]])

#edge case 3: single input
test_function([[1],[1]])

#edge case 4
test_function([[2,3],[3,2]])
