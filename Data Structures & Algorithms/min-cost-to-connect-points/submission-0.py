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
                if visit[i]: # node visited
                    continue
                curDist = (abs(points[i][0]- points[node][0])+ abs(points[i][1]-points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            edges += 1

        return int(res)

