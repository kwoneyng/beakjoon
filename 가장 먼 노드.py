from collections import deque

class Node:
    def __init__(self,num,depth):
        self.num = num
        self.depth = depth

class Graph:
    def __init__(self, nxtArr, n):
        self.nxtArr = nxtArr
        self.head = Node(1,0)
        self.vis = [0]*(n+1)
        self.max = 0
    
    def make_graph(self):
        head = self.head
        self.vis[1] = 1
        q = deque([head])
        answer = 1
        while q:
            cur = q.popleft()
            print('cur =',cur.num)
            for i in self.nxtArr[cur.num]:
                if self.vis[i] == 0:
                    nxt = Node(i,cur.depth+1)
                    print('nxt =',nxt.num, nxt.depth)
                    self.vis[i] = 1
                    if cur.depth + 1 > self.max:
                        self.max = cur.depth + 1
                        answer = 1
                    elif cur.depth + 1 == self.max:
                        answer += 1
                    q.append(nxt)
        return answer

        


def solution(n, edge):
    answer = 0
    nxtArr = [[] for i in range(n+1)]
    for a,b in edge:
        nxtArr[a].append(b)
        nxtArr[b].append(a)
    graph = Graph(nxtArr,n)
    return graph.make_graph()
    

n,edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))