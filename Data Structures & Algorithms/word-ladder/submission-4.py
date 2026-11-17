class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        words = set(wordList)
        res = 0
        q = deque([beginWord]) # Start at begin word

        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord: # Base Case
                    return res
                
                for i in range(len(node)):
                    for c in range(ord('a'), ord('z')+1):
                        if chr(c) == node[i]: # same char
                            continue
                        new_word = node[:i] + chr(c) + node[i+1:]
                        if new_word in words:
                            q.append(new_word)
                            words.remove(new_word)
        return -1
                        
                        

                    
