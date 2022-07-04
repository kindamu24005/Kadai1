
#計算の速さ→decimalを使う
from decimal import *
getcontext().prec=10000000
a,b=map(Decimal,input().split())
print(a+b)

#コード量の少なさ
print(sum(map(int,input().split())))