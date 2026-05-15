# https://atcoder.jp/contests/typical90/tasks/typical90_a
N, L = [int(s) for s in input().split()]
K = int(input())
A = [int(s) for s in input().split()]

# 切れ込みの部分 (先頭と末尾も含める)
cut_pos = [0] + A + [L]

def is_valid(mid):
    piece = 0
    curr = 0
    for pos in cut_pos:
        if pos - curr >= mid:
            piece += 1
            curr = pos
    
    return piece >= K + 1

# 1ピースの長さが何[cm]かで二分探索
ok, ng = 0, L + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    
    if is_valid(mid):
        ok = mid
    else:
        ng = mid

# 最短で ok [cm] になる
print(ok)
