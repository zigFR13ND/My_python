# utils.py

def is_prime(a):
    return f'{len([a % i for i in range(2, a + 1)]) > 2}


print(is_prime(4))