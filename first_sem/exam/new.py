a = [1, 2, 3, 4, 5, 6, 7, 8]
K = 3
n = 8

j = 0
t1 = None
t2 = a[0]

for i in range(n):
    j_new = (j - K) % n
    t1 = a[j_new]
    a[j_new] = t2
    t2 = t1
    j = j_new

print(a)
