def extgcd(a,b): #関数を定義(再起関数)

    if b == 0: #大÷小で割り切れたとき(終了条件)
        return 1,0,a #(X=1、Y=0、小さい方の数字)で出力

    q,r = a//b,a%b
    s,t,d = extgcd(b,r) #再帰関数の考え
    x,y = t,s-q*t
    return x,y,d

    
a,b = map(int, input().split())
x,y,c = extgcd(a,b)
print(x,y)