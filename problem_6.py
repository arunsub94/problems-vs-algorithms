def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    try:

        for x in ints:
            if not type(x) is int:
                raise TypeError

        min = ints[0]
        max = ints[0]

        for x in ints:
            if (x <= min):
                min = x
            if (x >= max):
                max = x

        return (min, max)

    except (IndexError, TypeError):
        print("Invalid input, please try again.")
        return False

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

#Edge case 1: empty input
l2 = [ ]
print ("Pass" if ((None, None) == get_min_max(l2)) else "Fail")

#Edge Case 2: Pretty big list
l3 = [ _ for _ in range(1, 200001)]
random.shuffle(l3)
print ("Pass" if ((1, 200000) == get_min_max(l3)) else "Fail")
