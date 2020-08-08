Explanation for Problem 5

This problem was relatively straightforward to implement since the markdown was pretty
self explanatory. The choice of Trie as a data structure makes sense due to the space efficiency
of Trie that allows multiple words to be stored in a concise fashion. The insertion/retrieval in the case of a dictionary
is O(1) and hence the time efficiency of insertion/retrieval from Trie is very attractive.

The time complexity of the find function is O(n), hence we would be iterating through each character of the prefix. The time
complexity of the suffix function is also O(n), since we could end up iterating through all nodes of Trie in the worst case, to find all suffixes from a particular node.
