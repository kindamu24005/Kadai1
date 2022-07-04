#引き算
#速さ重視(0.03秒)
from decimal import *
getcontext().prec=10000000
a,b=map(Decimal,input().split())
print(a+b)
#コード量重視(0.26秒)
a,b=map(int,input().split())
print(a-b)


#かけ算(掛け算はdecimal型でなくても計算が早い)
#0.02秒
a,b=map(int,input().split())
print(a*b)


#割り算
#0.02秒
a,b=map(int, input().split())
c=abs(a)//abs(b)
print(-c if a*b<0 else c)


#割り算の余り
#0.02秒
a,b=map(int,input().split())
print(a%b)


#掛け算2
#2.44秒
a,b=map(int,input().split())
print(a*b)
#0.06秒
from decimal import *
getcontext().prec=10000000
a,b=map(Decimal,input().split())
if a==0 or b==0: #これないと-0とか出てくる
    print(0)
else:
    print(a*b)