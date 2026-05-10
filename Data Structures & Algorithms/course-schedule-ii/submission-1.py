class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegree = [0]*numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        enrolled = 0
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            enrolled += 1
            for n in graph[node]:
                inDegree[n] -= 1
                if inDegree[n] == 0:
                    q.append(n)
        
        if enrolled != numCourses:
            return []
        return res