import string

def solution(msg):
    answer = []
    alpha = string.ascii_uppercase
    ht = {}
    for i,v in enumerate(list(alpha),start=1):
        ht[v] = i
    news = ''
    value = 0
    for c in msg:
        news += c
        if ht.get(news):
            value = ht[news]
        else:
            answer.append(value)
            ht[news] = len(ht)+1
            news = c
            value = ht[c]
    answer.append(value)
    return answer

m ="ABABABABABABABAB"
print(solution(m))

print(ord('A'))
print(chr(65))