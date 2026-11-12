class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If there is a cycle it is not a valid tree
        # Disconnected node
        # 
        # Idea 1, Map -> detect cycle, detect node not connected to others

        if n == 0:
            return True
            
        return False