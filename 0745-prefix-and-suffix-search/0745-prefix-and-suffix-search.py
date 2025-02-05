class TrieNode:
    def __init__(self):
        self.children = {}
        self.indexes = []
        self.isEnd = False

    def addIndex(self, index):
        self.indexes.append(index)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, index):
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
            current.addIndex(index)
        current.isEnd = True

    def search(self,word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.indexes

# need to store indexes in the nodes?
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.suftrie = Trie()
        for i, word in enumerate(words):
            self.trie.add(word, i)
            self.suftrie.add(reversed(word), i)

    def f(self, pref: str, suff: str) -> int:

        pref_indexes = self.trie.search(pref)
        suff_indexes = self.suftrie.search(suff[::-1])
        if not pref_indexes or not suff_indexes:
            return -1
        l = len(pref_indexes)-1
        r = len(suff_indexes)-1
        while l >= 0 and r >= 0:
            if pref_indexes[l] == suff_indexes[r]:
                return pref_indexes[l]
            elif pref_indexes[l] > suff_indexes[r]:
                l -= 1
            else:
                r -= 1
        return -1

        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

# is this a two trie problem?

# ex : apple ; a , e
# suffixtree - e l p p a
# prefixtree - a p p l e 

# list of hashmaps - word : trie
# ex: [apple, pear, testing]

# iterate from right to left of list
# if has prefix and suffix - return it
# if we get thru the whole list - return -1