class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for c in string:
            if c not in curr_node.children:
                curr_node.children[c] = Node(c)

            curr_node = curr_node.children[c]
        
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

def solution(words, queries):
    answer = []
    return answer

                
words, queries = ["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "prode"]
print('answer is')
print(solution(words,queries))