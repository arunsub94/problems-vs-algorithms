Explanation for Problem 2

In this problem, I have employed an algorithm to broadly accomplish three things:
    1. Get the pivot element around which the array is rotated
    2. A function that will get the pivot and search for the target after we split the array into two sorted segments around pivot.
    3. A binary search function to search for the target within the sorted segments of the array.

Time complexity analysis

  -> get_pivot function: This is a recursive function that looks for the pivot element
     at the middle indices during every recursive call. If not found, the function is recursively
     called after comparing the middle element to the start (based on the assumption that in a sorted array
     the middle element needs to be greater than the sorted array). If this does not hold good, we can infer that the
     pivot index is somewhere in the first half of this array. Else, it must be in the second half. Since the array is bisected at every recursive call this is an O(log n) function.

  -> rotated_array_search function: This is again a recurive function that employs binary search on the
     chunks of the array around the pivot. Since this function recursively calls binary search, the time complexity
     of this function is the same as that of binary search.

  -> binary_search function: The time complexity of binary search is O(log n).

  Hence, the time complexity of the algorithm is O(log n).
