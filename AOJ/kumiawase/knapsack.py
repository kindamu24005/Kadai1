n,W=map(int,input().split())

#一般のナップサック問題は列を回すときに前から回すように変える
dp=[0 for j in range(W+1)]
for i in range(n):
    v,w=map(int,input().split())
    #0-1ナップサック問題の時は、range(W,w-1,-1)で回した
    for j in range(w,W+1):
        dp[j]=max(dp[j],dp[j-w]+v)
print(dp[W])