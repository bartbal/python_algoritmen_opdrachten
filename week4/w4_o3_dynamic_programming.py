def B(n, k):
    assert k <= n, "k has to be smaller or equal to n"
    assert k > 0 or n > 0, "parameters have to be equal or more than 0"
    tabel = []
    for N in range(n+2):
        tabel.append([])
        for K in range(N):
            if K == 0:
                tabel[N].append(1)
                continue
            if(len(tabel[N-1])-1 < K ):
                tabel[N].append(tabel[N-1][K-1])
                continue

            tabel[N].append(tabel[N-1][K] + tabel[N-1][K-1])
    tabel.pop(0)
    print(tabel)
    return tabel[n][k]

print(B(6,3))

# n = y
# k = x