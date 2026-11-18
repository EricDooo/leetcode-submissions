class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0 # index of starting node
        dist = [math.inf] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n-1: # We want to find all edges, edges for connecting all is n-1
            visit[node] = True # visit current node
            nextNode = -1
            for i in range(n):
                if visit[i]: # node visited, quick break
                    continue
                curDist = (abs(points[i][0]- points[node][0])+
                            abs(points[i][1]-points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]: # compare distances each node to set
                    nextNode = i

            res += dist[nextNode] # Choose the node
            node = nextNode
            edges += 1 # found an edge, increment

        return int(res)

