import fractions, math
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 2])
    return arr
A, B = map(int, input().split())
N = fractions.gcd(A, B)
prime_list = factorization(N)
if N == 1:
    print(1)
else:
    print(len(prime_list)+1)
