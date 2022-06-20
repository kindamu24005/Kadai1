from functools import reduce
import math

#最小公倍数の定義
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

n = int(input())
a = list(map(int, input().split()))
#reduce()でリストaの要素に順番に最小公倍数の定義を当てはめていく
print(reduce(lcm,a))