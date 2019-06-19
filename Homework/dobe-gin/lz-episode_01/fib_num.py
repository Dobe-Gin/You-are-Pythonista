def fibs(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


if __name__ == '__main__':
    fib_list = list(fibs(10))
    print(fib_list)
