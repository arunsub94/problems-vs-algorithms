# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.root.insert('/', handler)

    def insert(self, pathList, path_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        path_str = ''
        current_node = self.root
        for path_char in pathList:
            if path_char not in current_node.children:
                current_node.insert(path_char)
            path_str += path_char
            current_node = current_node.children[path_char]
        #Set deepest node (leaf) handler as path handler
        current_node.handler = path_handler

    def find(self, pathList):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root
        for path_char in pathList:
            if (path_char in current_node.children):
                current_node = current_node.children[path_char]
            else:
                return None

        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path_char, path_handler = None):
        # Insert the node as before
        self.children[path_char] = RouteTrieNode(path_handler)

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.rTrie = RouteTrie(handler)

    def add_handler(self, path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        pathList = self.split_path(path)
        self.rTrie.insert(pathList, path_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        if (path == '/'):
            return self.rTrie.find('/')

        pathList = self.split_path(path)
        return self.rTrie.find(pathList)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        splitted_path= list(filter(None, path.split('/')))
        return splitted_path

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

#Test Case 2

router2 = Router("root handler")
router2.add_handler("/TheSopranos/characters/TonySoprano", "Tony handler")
router2.add_handler("/TheSopranos/characters/CarmelaSoprano", "Carmela handler")
router2.add_handler("/TheSopranos/characters/AnthonyJrSoprano", "Tony Jr. handler")
router2.add_handler("/TheSopranos/characters/MeadowSoprano", "Meadow handler")

#some lookups
print(router2.lookup("/")) #should return root handler
print(router2.lookup("/TheSopranos/characters/TonySoprano")) #should return Tony handler
print(router2.lookup("/TheSopranos/characters/CarmelaSoprano/")) #should return Carmela handler
print(router2.lookup("/TheSopranos/characters/JaniceSoprano/")) #should return None

#Test Case 3

router3 = Router("root handler")
router3.add_handler("/home/", "home is where the heart is")

print(router3.lookup("/home")) #should return home is where the heart is
print(router3.lookup("/")) #should return root handler`
print(router3.lookup("/home/lungs/")) #should return None
