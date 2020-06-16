arr = ["1", "-", "3", "+", "5", "-", "8"]

# 순열은 말도 안된다.
# 100개 이므로 순열만 아니면 될듯한데
# 계산을 여러번 할 때에는 DP를 이용해보자
# 계산이 총 n몇번 일어났는지를 파악하면 DP를 이용해 설계하기에 편하다 플로이드 워셜과 비슷한 방식으로 구성한다.

n = len(arr)//2 + 1 

max_arr = [[-1000000000]*n for i in range(n)]
min_arr = [[1000000000]*n for i in range(n)]

for i in range(n):
	max_arr[i][i] = int(arr[i*2])
	min_arr[i][i] = int(arr[i*2])

for c in range(n):
	for x in range(n-c):
		y = x+c
		for k in range(y):
			if arr[k*2+1] == '+':
				max_arr[x][y] = max(max_arr[x][k]+max_arr[k+1][y], max_arr[x][y])
				min_arr[x][y] = min(min_arr[x][k]+min_arr[k+1][y], min_arr[x][y])
			else:
				max_arr[x][y] = max(max_arr[x][k]-min_arr[k+1][y], max_arr[x][y])
				min_arr[x][y] = min(min_arr[x][k]-max_arr[k+1][y], min_arr[x][y])

print(max_arr[0][n-1])