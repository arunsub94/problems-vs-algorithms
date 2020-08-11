Explanation for Problem 5

This problem was relatively straightforward to implement since the markdown was pretty
self explanatory. The choice of Trie as a data structure makes sense due to the space efficiency
of Trie that allows multiple words to be stored in a concise fashion. The insertion/retrieval in the case of a dictionary
on average is O(1) (and worst case O(n)) and hence the time efficiency of insertion/retrieval from Trie is very attractive.

The time complexity of the find function is O(m*n), since we would be iterating through the prefix (of size m) and in the worst case, looking up the dictionary would be O(n).
The time complexity of the suffix function is also O(m*n), since we could end up iterating through all nodes of Trie in the worst case, to find all suffixes from a particular node.

Hence, the time complexity of the algorithm would be O(m*n).

The space complexity of the Trie data structure is dependent on the count of each character (c) and average word length (w), and hence the space complexity would be O(c*w).
