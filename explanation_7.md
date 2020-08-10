Explanation for Problem 7

The path handler system leverages the Trie's space efficiency to store many paths.

The insert and lookup operations both are of O(m*n) time complexity since each path could be of size m and insertion and lookup operations in the worst case could be O(n).

The algorithm's time complexity is O(m*n)

My code can handle stray slashes but I have not included a "not found" handler.
