def sosuhantei(n): #素数判定の定義
  if n == 2: #2は素数
    return True
  if n < 2 and n % 2 == 0: #2より下の数(1)と2で割り切れる数(偶数)は素数じゃない
    return False
  for i in range(3, int((n**0.5)+1), 2): #合成数の定理
    if n%i == 0:
      return False
  return True

#素因数分解してリストを作る
N = int(input())
n = N
ans = []
for j in range(2, int((n**0.5)+1)): #素数判定を使う
  if sosuhantei(j) == True: #素数なら割り切れるまで割る
    while n % j == 0:
      n/=j
      ans.append(j)
if n != 1: #残ったNが1ではない(素数)の時
  ans.append(int(n))

#ファイ関数の定義に当てはめる
import math
a = 1
for i in set(ans): #リストの重複しているものを削る
  N *= (1-1/i)
print(int(N))
