# Calculating the square root of a number

def sqrt(number):

    """ Input: int - number whose square root needs to be found
        Output: int - floor value of square root
        This function takes a number and returns the floor value of its square root
        without using built-in Python functions."""

    start = 0
    end = number//2

    if number == 1:
        return 1
    else:
        while (start <= end):
            mid = (start + end)//2
            sqr = mid * mid
            if (sqr == number):
                return mid
            elif (sqr > number):
                end = mid - 1
            elif (sqr < number):
                potential_floor = mid
                start = mid + 1

    return potential_floor

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
