n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    ns = []
    for i in range(1, n+1):
        if n % i == 0:
            ns.append(i)
    gcds = []
    for g in ns:
        if m % g == 0:
            gcds.append(g)
    
    gcd = max(gcds)

    print(gcd)

gcd(n, m)
