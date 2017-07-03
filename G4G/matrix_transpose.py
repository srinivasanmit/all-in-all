m = [[1,2],[3,4],[5,6]]
for row in m :
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)

res = [ [0,0,0], [0,0,0] ]
for c in range(len(m) - 1) :
    for r in range(len(row) -1) :
        print r,c
        res[c][r] = m[r][c]
for row in res :
    print(row)
