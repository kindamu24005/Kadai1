n,W=map(int,input().split())

#dp[i][j]=i番目までの品物を使って容量jを超えないようにした時の価値の最大値
#行列を作る
dp=[[0 for j in range(W+1)] for i in range(n)]

#dp[i][j]を規則に従って埋めていく
for i in range(n):
  v,w=map(int,input().split())
  for j in range(W+1):
    if j>=w:
      dp[i][j]=max(dp[i-1][j],v+dp[i-1][j-w])
    else:
      dp[i][j]=dp[i-1][j]

print(dp[n-1][W])


#######ナップサック問題もコイン問題同様一次元配列で求まる

n,W=map(int,input().split())
dp=[0 for j in range(W+1)]
for i in range(n):
    v,w=map(int,input().split())
    #列を回すときは後ろから回していくことに注意！！！！！！！！！！！！！！！！
    for j in range(W,w-1,-1):
        dp[j]=max(dp[j],dp[j-w]+v)
print(dp[W])
