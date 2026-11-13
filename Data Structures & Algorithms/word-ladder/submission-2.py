class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # O(n * m) for searching end word in word list
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        words, res = set(wordList), 0 # O(n) for converting to set
        q = deque([beginWord])

        while q: # O (n)
            res += 1 # increment depth
            for _ in range(len(q)):
                node = q.popleft() # Next word in each level trav
                if node == endWord: # First found is shortest path
                    return res
                
                for i in range(len(node)): # O(m)
                    for c in range(ord('a'), ord('z')+1): # O(26)
                        if chr(c) == node[i]:
                            continue
                        # O(m) for copying strings
                        nei = node[:i] + chr(c) + node[i + 1:]
                        if nei in words: # O(1) in python hashset
                            q.append(nei) # Add to next level of bfs
                            words.remove(nei) # No words get used twice
        return 0