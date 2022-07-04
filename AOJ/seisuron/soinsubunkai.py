def sosuhantei(n): #素数判定の定義
  if n == 2: #2は素数
    return True
  if n < 2 and n % 2 == 0: #2より下の数(1)と2で割り切れる数(偶数)は素数じゃない
    return False
  for i in range(3, int((n**0.5)+1), 2): #合成数の定理
    if n%i == 0:
      return False
  return True

N = int(input())
print(N, end=": ")
ans = []
for j in range(2, int((N**0.5)+1)): #素数判定を使う
  if sosuhantei(j) == True: #素数ならその数で割り切れるまで割る
    while N % j == 0:
      N /= j
      ans.append(j)

if N != 1: #残ったNが1ではない(素数)の時
  ans.append(int(N))


print(*ans)