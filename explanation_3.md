Explanation for Problem 3

The rearranging digits problems requires that the array be sorted in the ascending order
and then picking out the digits to fill up the numbers.

For the sorting algorithm, I have employed merge sort which is of O(nlogn) time complexity.
After sorting the array, I have employed a for loop to run through the digit positions. Since the number of digits
follows a log n (base 10) relationship with input size n, the time complexity of this for loop is O(log n).

Hence, the time complexity of the algorithm can be said to be strictly O(nlogn) + O(logn). Since O(logn) < O(nlogn),
we can approximate worst case complexity to O(nlogn). This also intuitively makes sense since the algorithm is essentially
a merge sort.

Space complexity: The worst case space complexity of merge sort is O(n), along with an O(log n) complexity for the numbers since the number of digits follows a log 10 relationship with size of input and hence the space complexity of the algorithm is O(n).
