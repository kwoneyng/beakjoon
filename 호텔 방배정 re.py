import sys
sys.setrecursionlimit(10000)

def find(n,ht):
    if ht[n] == n:
        ht[n] += 1
        return n
    else:
        room = find(ht[n],ht)
        ht[n] = room + 1
        return room

def solution(k, room_number):
    answer = []
    room = {}
    for i in range(1,k+1):
        room[i] = i
    
    for num in room_number:
        empty = find(num,room)
        answer.append(empty)
    
    return answer

k, room_number = 10,[1,3,4,1,3,1]	
print(solution(k,room_number))

# def findEmptyRoom(number, rooms): # 빈방을 찾는 함수
#     if number not in rooms:        
#         rooms[number] = number + 1
#         return number
    
#     empty = findEmptyRoom(rooms[number], rooms)
#     rooms[number] = empty + 1
#     return empty


# def solution(k, room_number):
#     answer = []
#     rooms = dict() # 몇번 방이 비어있는지 체크하는 딕셔너리

#     for number in room_number:
#         emptyRoom = findEmptyRoom(number, rooms)
#         answer.append(emptyRoom)
    
#     return answer