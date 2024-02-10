import time


def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


def main():
    @clock
    def func_ex(n):
        a = list(range(1, n))
        return sum(a)

    func_ex(1_000_000)


if __name__ == '__main__':
    main()