class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # topological sort
        # check if there is a cycle
        adj = defaultdict(set)
        in_deg = {}
        char_set = set()
        max_len = max(len(word) for word in words)

        for i in range(1,len(words)):
            prev_word, next_word = words[i-1], words[i]
            minlen = min(len(prev_word),len(next_word))
            if prev_word[:minlen] == next_word[:minlen] and len(prev_word) > len(next_word):
                return ""
            for j in range(minlen):
                if prev_word[j] != next_word[j]:
                    if next_word[j] not in adj[prev_word[j]]:
                        adj[prev_word[j]].add(next_word[j])
                        in_deg[next_word[j]] = in_deg.get(next_word[j], 0) + 1
                    break
                
        for word in words:
            for char in word:
                char_set.add(char)
        for char in char_set:
            if char not in in_deg:
                in_deg[char] = 0
        
        '''
        for word in words:
            char_set.add(word[0])
            if word[0] not in in_deg:
                in_deg[word[0]] = 0

            for i in range(1, len(word)):
                if word[i] != word[i-1]:
                    if word[i] not in adj[word[i-1]]:
                        adj[word[i-1]].add(word[i])
                        in_deg[word[i]] = in_deg.get(word[i],0) + 1
                    char_set.add(word[i])
        '''
        
        q = deque([])
        for char in in_deg.keys():
            if in_deg[char] == 0:
                q.append(char)

        visited = set()
        res = ""
        while q:
            current = q.popleft()
            if current in visited:
                continue
            res += current
            visited.add(current)
            for nei in adj[current]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    q.append(nei)

        return res if len(res) == len(in_deg) else ""
