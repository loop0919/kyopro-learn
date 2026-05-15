# https://atcoder.jp/contests/abc388/tasks/abc388_c
N = int(input())
A = [int(s) for s in input().split()]

A.sort()
ans = 0

for a in A:
    ok, ng = 0, N + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        
        if A[mid - 1] <= a // 2:
            ok = mid
        else:
            ng = mid
    
    ans += ok

print(ans)
