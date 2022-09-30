import bisect
n=int(input())
inf=float("inf")
#dp行列を作る
dp=[inf]*n
#数列の個数で回す
for _ in range(n):
  a=int(input())
  #bisect_left：ソートされた数列の中に数字を追加するとき
  #追加する数字が複数ある場合、その数字の一番左のインデックスを返す
  i=bisect.bisect_left(dp,a)
  dp[i]=a

print(bisect.bisect_left(dp,inf))