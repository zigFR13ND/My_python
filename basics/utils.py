# utils.py

def is_prime(n):
    # возвращает True, если число простое, и False иначе.
    ln = []
    for i in range(1, n + 1):
        if n % i == 0:
            ln.append(i)
    return len(ln) <= 2


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)