def solution(board, moves):
    stack = []
    answer = 0
    size = len(board)
    
    def pick(x):
        for i in range(size):
            if board[i][x] > 0:
                target, board[i][x] = board[i][x], 0
                return target
    
    for t in moves:
        target = pick(t-1)
        if target:
            stack.append(target)
            if len(stack) > 1:
                if stack[-1] == stack[-2]:
                    answer += 2
                    stack = stack[:-2]
    
    return answer