# https://atcoder.jp/contests/abc231/tasks/abc231_c
N, Q = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

# A をソートし、 A[0] < A[1] < ... < A[N - 1] にする.
A.sort()

for _ in range(Q):
    x = int(input())

    ok, ng = 0, N + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2

        # A[N - mid], A[N - mid + 1], ..., A[N - 1] の mid 個が
        # x 以上ならば条件を満たす.
        if A[N - mid] >= x:
            ok = mid
        else:
            ng = mid

    print(ok)
