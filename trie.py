class TrieNode(object):

    def __init__(self, word=None):
        """Initialize this trie node."""
        self.word = word
        self.children = [None] * 27

    def __repr__(self):
        """Return a string representation of this trie node."""
        return 'TrieNode({!r})'.format(self.children)

    def is_leaf(self):
        """Return True if this node is a leaf (all children are None)."""
        for child in self.children:
            if child != None:
                return False
        return True

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.is_leaf() == False

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""
        height = 0
        heights = [height]
        for child in self.children:
            if child != None:
                heights.append(child.height() + 1)
        return max(heights)


class Trie(object):

    def __init__(self, words=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = TrieNode()
        self.size = 0
        if words != None:
            for path in words:
                self.insert(path)

    def __repr__(self):
        """Return a string representation of this trie."""
        return 'Trie({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this trie is empty (has no nodes)."""
        return self.root.is_leaf()

    def height(self):
        """Return the height of this trie (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node)."""
        if self.is_empty() == False:
            return self.root.height()

    def search(self, word):
        """Return the price of the call for the number input."""
        current = self.root
        for let in word:
            key = ord(let.lower()) - 97
            if current.children[key] is not None:
                current = current.children[key]
            else:
                break

        return current.word

    def insert(self, letter_path):
        """Insert the path of the words into this trie."""
        current = self.root
        for let in letter_path:
            key = ord(let.lower()) - 97
            if let == ' ':
                key = 26
            print(key, let.lower())
            if current.children[key] == None:
                current.children[key] = TrieNode(letter_path)
                self.size += 1
            current = current.children[key]
            if current.word == None:
                current.word = letter_path
