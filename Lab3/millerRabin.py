import random

def is_prime_miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Express n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

if __name__ == "__main__":
    n = int(input("Enter a number to test for primality: "))
    k = int(input("Enter the number of rounds (recommended: 5): "))

    if is_prime_miller_rabin(n, k):
        print(f"{n} is likely a prime number.")
    else:
        print(f"{n} is a composite number.")
