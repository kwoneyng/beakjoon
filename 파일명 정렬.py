class File:
    def __init__(self,file):
        self.filename = file
        self.head = ''
        self.number = ''
        self.tail = ''
        n = len(file)
        start = 0
        for i in range(start,n):
            cur = file[i]
            if not cur.isdigit():
                self.head += cur.upper()
            else:
                start = i
                break
        for i in range(start,n):
            cur = file[i]
            if cur.isdigit():
                self.number += cur
            else:
                start = i
                break
        self.tail = file[start:]
        self.number = int(self.number)

def solution(files):
    answer = []
    arr =[]
    for i in files:
        fi = File(i)
        arr.append(fi)
    arr.sort(key=lambda x: x.number)
    arr.sort(key=lambda x: x.head)
    for item in arr:
        answer.append(item.filename)

    return answer
f = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(f))