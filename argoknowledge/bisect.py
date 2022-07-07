import bisect

A = [1,2,2,2,3,3,4,5,5,5,6,6,6]
x = bisect.bisect_left(A,3)
y = bisect.bisect_right(A,4)

print(x,y)