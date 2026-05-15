# https://atcoder.jp/contests/abc231/tasks/abc231_c
from bisect import bisect_left

N, Q = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

# A をソートし、 A[0] < A[1] < ... < A[N - 1] にする.
A.sort()

for _ in range(Q):
    x = int(input())

    # A[idx] >= x となる最小の idx
    idx = bisect_left(A, x)

    # A[idx], A[idx + 1], ... , A[N - 1] の N - idx 人が答え
    ans = N - idx

    print(ans)
