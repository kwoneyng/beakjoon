import re

def solution(files):
    temp = []
    for file in range(len(files)):
        head, number, tail = re.split('[0-9]+', files[file])  # 정규식 사용(숫자 기준으로 나눈다 : 문제에서 숫자는 가운데 말고 나오지 않는다.)
        temp.append((head, number, tail))
    print(temp)
    temp_sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1]), x[2]))

    answer = []
    for i in temp_sort:
        answer.append(files[i[2]])

    return answer

files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']
print(solution(files))