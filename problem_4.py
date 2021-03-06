def sort_dutch(arr):
    try:
        for el in arr:
            if (el not in [0,1,2]):
                raise ValueError
    except ValueError:
        print("Sorry, input must contain only 0, 1 or 2")
        return False

    #Two pointers for the next 0 position and 2 position
    pointer_0 = 0
    pointer_2 = len(arr) - 1

    index = 0
    while index <= pointer_2:
        if(arr[index] == 0):
            arr[index] = arr[pointer_0]
            arr[pointer_0] = 0
            pointer_0 += 1
            index += 1
        elif(arr[index] == 2):
            arr[index] = arr[pointer_2]
            arr[pointer_2] = 2
            pointer_2 -= 1
        else:
            arr[index] = 1
            index += 1

    return arr

def test_function(test_case):
    dutch_array = sort_dutch(test_case)
    if dutch_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0,2,1,1,2,0,0])
test_function([1,0])
test_function([2,1])
test_function([1,1,1])

#edge case 1
test_function([])

#edge case 2: a large reversed sorted list
test_list=[2]*100+[1]*120+[0]*200
test_function(test_list)

#edge case 3: invalid input (other than 0,1 or 2)
test_function([0,1,2,3])
