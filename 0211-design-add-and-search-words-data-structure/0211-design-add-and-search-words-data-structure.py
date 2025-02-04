class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

# dfs search every time we see a dot?
# only two dots !
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isEnd = True

    def search(self, word: str) -> bool:
        # we can't start over from root - need to pass in current trie node
        print(word)
        current = self.root
        for i, char in enumerate(word):
            if char != '.':
                if char not in current.children:
                    print("testing")
                    return False
            else:
                possible_letters = current.children.keys()
                for letter in possible_letters:
                    possible_str = letter + word[i+1:]
                    if self.search_with_node(possible_str, current):
                        return True
                return False
            
            current = current.children[char]
        
        return current.isEnd

    def search_with_node(self, word: str, current) -> bool:
        # we can't start over from root - need to pass in current trie node
        for i, char in enumerate(word):
            if char != '.':
                if char not in current.children:
                    print("testing")
                    return False
            else:
                possible_letters = current.children.keys()
                for letter in possible_letters:
                    possible_str = letter + word[i+1:]
                    if self.search_with_node(possible_str, current):
                        return True
                return False
            
            current = current.children[char]
        
        return current.isEnd


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)