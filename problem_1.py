# Calculating the square root of a number

def sqrt(number):

    """ Input: int - number whose square root needs to be found
        Output: int - floor value of square root
        This function takes a number and returns the floor value of its square root
        without using built-in Python functions."""

    try:
        if not type(number) is int:
            raise TypeError("Only integers are allowed")

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

    except TypeError:
        print("Sorry, input is not a valid number!")
        return False

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

#Edge Case 1
print ("Pass" if  (None == sqrt(None)) else "Fail") #should raise exception
#Edge Case 2
print ("Pass" if  (0.07071 == sqrt(0.005)) else "Fail") #should raise exception
#Edge Case 3
print ("Pass" if  (100 == sqrt(10000)) else "Fail")
