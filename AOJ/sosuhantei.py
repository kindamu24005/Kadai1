def isprime(x):
	if x == 2: #2は素数
		return True
	if x < 2 or x % 2 == 0: #2以下と2で割り切れない数（偶数）は素数じゃない
		return False
	for i in range(3, int(x**0.5) + 1, 2): #合成数の定理を使って判定範囲を削る
		if x % i == 0:
			return False
		i += 2
	return True

N = int(input())
c = 0
for i in range(N):
	c += int(isprime(int(input())))
print(c)