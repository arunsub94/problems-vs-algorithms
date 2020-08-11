Explanation for Problem 4

This logic was discussed in the Udacity course problem Sort-0-1-2. This problem demands the exact same approach. Any similarities are owing to the fact that these two problems are one and the same.

We know that the 0s lump together at the start and all the 2s can be found at the end.
Since the constraint is one of single traversal, we employ pointers to keep tabs on the next 0 position and
the next 2 position and since we know that it's either 0, 1 or 2 in the array, the only other option left is 1.
We fill the array up in this way using a while loop, making the time complexity of the algorithm O(n).

Since this algorithm uses three pointers and loops through the input, it has O(n) space complexity. 
