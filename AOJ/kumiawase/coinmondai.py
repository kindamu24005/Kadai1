n,m=map(int,input().split())
c = list(map(int,input().split()))

"""
使えるコインの種類(ci)を行、支払う金額(n+1)列として
使用するコインの枚数を要素にもつ行列を作る(0円の支払いを加えるため→n+1)
"""
#初期値として行列の値は全てinfに設定
inf = float("inf")
dp=[[inf for x in range(n+1)] for y in range(m)]

#行列の値を埋めていく
#支払額が0円の時は、コインの枚数は0枚
for k in range(m):
  dp[k][0] = 0
#漸化式を用い残りの要素を埋める
for j in range(n+1):
  for i in range(m):
    if j < c[i]:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = min(dp[i-1][j],dp[i][j-c[i]]+1)
print(dp[m-1][n])
###早さ00.96 s メモリ43508 KB コードの量330 B###



#######求める値はm行目であるため、それ以前の行は必要ない#######
#使えるコインの種類が増えたら行を上書きすればOK
#一次元の行列のみで表せる
inf = float("inf")
dp=[inf for x in range(n+1)]
#最初の要素は0円の支払いだから使うコインは0枚
dp[0]=0
#コインの種類の中で回す
for i in c:
  #コインの種類の値から支払う額の+1まで回す
  for j in range(i,n+1):
    #要素を埋める
    dp[j] = min(dp[j],dp[j-i]+1)
print(dp[n])
###早さ00.52 s メモリ7652 KB コードの量202 B###