# https://atcoder.jp/contests/abc388/tasks/abc388_c
from bisect import bisect_right

N = int(input())
A = [int(s) for s in input().split()]

A.sort()
ans = 0

for a in A:
    ans += bisect_right(A, a // 2)

print(ans)
