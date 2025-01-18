class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # just add #i?
        res = ""
        for i,string in enumerate(strs):
            res += "#" + str(len(string)) + "#" + string
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            if s[i] == "#":
                length = ""
                i += 1
                while s[i] != "#":
                    length += s[i]
                    i += 1
                i += 1
            #5#hello
            res.append(s[i:i + int(length)])
            i += int(length)
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))