# Creating a TrieNode which represents a letter, but we are not storing the letter rather trying to figure out if we have stored a certain word in the Trie, and we traverse the Trie through the children, which contain other TrieNodes, creating a tree of sorts. 
class TrieNode:
    def __init__(self):
        self.children = {}
        # We add a end of word flag to see if this word is in the list, this is specifically for the search function 
        self.endOfWord = False

class PrefixTree:
    # All we need is a root for the trie 
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        # We start at the root 
        cur = self.root

        for c in word:
            # If the letter is not in our TrieNode, we want to create it from this point onwards 
            if c not in cur.children:
                # So we give this child a trie node
                cur.children[c] = TrieNode()
            # Then we traverse the tree creating TrieNodes where needed as we explore the tree 
            cur = cur.children[c]
        # We want to switch the flag so that we know that this word has been added to the Trie 
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        # We search from the root 
        cur = self.root

        # For each letter in the word we want to see if the trie has that letter and move through until we get to the end of the word 
        for c in word:
            if c not in cur.children:
                return False
            # We want to explore further down the tree, so we loop until all letters are complete
            cur = cur.children[c]
        # Which at the point, cur will be the last letter of the word, where we check if we actually have the word in the tree not, just the prefix. 
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        # This is the same as the search algorithim except instead of returning cur.endOfWord, since we don't care if it is the end of the word or not we just return true if the loop completes successfully. 
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        return True 
        