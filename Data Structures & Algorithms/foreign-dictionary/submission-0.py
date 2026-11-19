class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {letter: set() for word in words for letter in word}
        indegree = {letter: 0 for letter in graph}
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]

            if len(first) > len(second) and first.startswith(second):
                return ""

            for a, b in zip(first, second):
                if a == b:
                    continue

                if b not in graph[a]:
                    graph[a].add(b)
                    indegree[b] += 1

                break
        queue = deque(letter for letter in indegree if indegree[letter] == 0)
        order = []

        while queue:
            letter = queue.popleft()
            order.append(letter)

            for neighbor in graph[letter]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(graph):
            return ""

        return "".join(order)