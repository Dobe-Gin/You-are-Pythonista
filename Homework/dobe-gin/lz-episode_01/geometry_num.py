from math import sqrt


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    prime_list = [i for i in range(1, 1000000) if is_prime(i)]
    print(prime_list)
