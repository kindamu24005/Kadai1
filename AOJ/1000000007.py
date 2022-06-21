m,n = map(int,input().split())
print(pow(m,n,1000000007)) #mのn乗を1000000007（1e+9より大きい最小の素数らしい）で割ったあまり

#こっちだとタイムオーバー
m,n = map(int,input().split())
ans = int(m**n % 1000000007)
print(ans)