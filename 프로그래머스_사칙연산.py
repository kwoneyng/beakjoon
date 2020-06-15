arr = ["1", "-", "3", "+", "5", "-", "8"]

# 순열은 말도 안된다.
# 100개 이므로 순열만 아니면 될듯한데
# 계산을 여러번 할 때에는 DP를 이용해보자
# 계산이 총 n몇번 일어났는지를 파악하면 DP를 이용해 설계하기에 편하다 플로이드 워셜과 비슷한 방식으로 구성한다.

maxcalc = [[-1000000]*(len(arr)//2 +1) for i in range(len(arr)//2 +1)]
mincalc = [[1000000]*(len(arr)//2 +1) for i in range(len(arr)//2 +1)]
n = len(maxcalc)

for i in range(len(arr)):
	if i % 2 == 0:
		j = i//2
		maxcalc[i//2][i//2] = int(arr[i])
		mincalc[i//2][i//2] = int(arr[i])

for i in maxcalc:
	print(i)

for c in range(1,n):
	for x in range(n-c):
		y = c+x
		