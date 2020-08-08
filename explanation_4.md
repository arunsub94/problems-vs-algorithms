Explanation for Problem 4

We know that the 0s lump together at the start and all the 2s can be found at the end.
Since the constraint is one of single traversal, we employ pointers to keep tabs on the next 0 position and
the next 2 position and since we know that it's either 0, 1 or 2 in the array, the only other option left is 1.
We fill the array up in this way using a while loop, making the time complexity of the algorithm O(n).
