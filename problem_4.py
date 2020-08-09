def sort_dutch(arr):

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
    print(dutch_array)
    if dutch_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0,2,1,1,2,0,0])
test_function([1,0])
test_function([2,1])
test_function([1,1,1])
