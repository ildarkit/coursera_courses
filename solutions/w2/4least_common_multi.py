# Uses python3


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == '__main__':
    p = map(int, input().split())
    print(lcm(*p))