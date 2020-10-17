def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        line = m-1
        for r in range(len(board)):
            if board[r][line] >0:
                target = board[r][line]
                board[r][line] = 0
                if stack and stack[-1] == target:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(target)
                break
    return answer

solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])