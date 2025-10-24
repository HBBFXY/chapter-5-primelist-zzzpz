def PrimeList(N):
    if N <= 2:
        return ""
    primes = []
    # 单独处理2（唯一的偶数质数）
    if N > 2:
        primes.append("2")
    # 只遍历奇数（从3开始，步长为2）
    for num in range(3, N, 2):
        is_prime = True
        # 同样只判断奇数除数，减少循环次数
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return " ".join(primes)
