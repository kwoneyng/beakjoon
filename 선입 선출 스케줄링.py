def solution(n, cores):
    mxt = max(cores)*n//len(cores)
    mnt = min(cores)*n//len(cores)
    while mnt < mxt:
        cnt = 0
        zero = 0
        mmt = (mnt+mxt)//2
        for i,core in enumerate(cores):
            cnt += mmt//core + 1
            if mmt%core == 0:
                cnt -= 1 
                zero += 1
        if cnt >= n:
            mxt = mmt
        elif cnt+zero < n:
            mnt = mmt+1
        else:
            for i,core in enumerate(cores):
                if mmt % core == 0:
                    cnt += 1
                    if cnt == n:
                        return i+1


n,c = 6, [1, 2, 3]
print(solution(n,c))
