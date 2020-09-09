def solution(s):
    s=s[1:-1]
    arr = []
    string = ''
    item = []
    for i in s:
        if i == '{':
            pass
        elif i == '}':
            item.append(int(string))
            arr.append(item)
            string = ''
            item = []
        elif i == ',':
            if not item and not string:
                continue
            item.append(int(string))
            string = ''
        else:
            string += i
    arr.sort(key=lambda x:len(x))
    return arr

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")