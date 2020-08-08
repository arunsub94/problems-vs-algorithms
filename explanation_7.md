Explanation for Problem 7

The path handler system leverages the Trie's space efficiency to store many paths.
The insert operation on the node takes O(1) time and the insertion of path function within the Trie
takes O(n) depending on the input size of the path. The lookup function also takes O(n) time due to the size
of the input list.

My code can handle stray slashes but I have not included a "not found" handler.
