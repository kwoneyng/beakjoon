def solution(brown, yellow):
    mm = brown//2

    for i in range(3,mm):
        for j in range(3,mm):
            if (i-2)*(j-2) == yellow and (i-2)*2 + (j-2)*2 + 4 == brown:
                return [j,i]