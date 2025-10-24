def PrimeList(N):
    if N <= 2:
        return ""
    primes = []
    # 从2开始判断，2是质数
    for num in range(2, N):
        is_prime = True
        # 优化：除数只需遍历到num的平方根
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return " ".join(primes)
