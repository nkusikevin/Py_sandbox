def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]

# Example usage
n = int(input("Enter the value of n: "))
nth_prime = find_nth_prime(n)
print(f"The {n}th prime number is: {nth_prime}")

