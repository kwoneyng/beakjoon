def make(nums,d,arr,vis=[]):
    if len(vis) == d:
        num = ''
        for v in vis:
            num += arr[v]
        nums.append(int(num))
        return
    for i in range(len(arr)):
        if i not in vis:
            vis.append(i)
            make(nums,d,arr,vis)
            vis.pop()
    
def solution(numbers):
    answer = 0
    n = 10**len(numbers)
    l = len(numbers)
    era = [0]*n
    primes = {}
    for i in range(2,n):
        if not era[i]:
            primes[i] = 1
            for j in range(2*i,n,i):
                era[j] = 1
        
        
    arr = list(numbers)
    nums = []
    for i in range(1,l+1):
        make(nums,i,arr)
    
    for num in nums:
        if primes.get(num) == 1:
            answer +=1
            primes[num] = 0
    return answer

n = '17'
print(solution(n))