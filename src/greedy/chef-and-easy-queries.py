# https://www.codechef.com/OCT20B/problems/CHEFEZQ

import inspect


Infinity = float('inf')


def integer_array_input():
    return MyList(map(int, input().split()))


def string_array_input():
    return MyList(map(String, input().split()))


def integer_input():
    return int(input())


def float_input():
    return float(input())
    

def string_input():
    return String(input())


def test_case_count():
    return range(integer_input())


def is_digit(character):
    return character in "0123456789"


def is_prime(n):
    if n <= 3:
        return n > 1
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


def sieve_of_eratosthenes(n):
    array = [True] * (n + 1)

    i = 2
    while i * i <= n:
        if array[i]:
            for j in range(i * i, n + 1, i):
                array[j] = False
        i += 1
    
    return [i for i in range(2, n + 1) if array[i]]


class This:
    def __init__(self):
        self.max = self.min = self.sum = self.count = None
        self.set = set()
        self.map = dict()
        self.reset()

    def update_if_max(self, *values):
        self.max = max(self.max, *values)

    def update_if_min(self, *values):
        self.min = min(self.min, *values)

    def reset(self):
        self.min = Infinity
        self.max = -Infinity
        self.sum = 0
        self.count = 0


class MyList(list):
    @property
    def length(self):
        return len(self)

    @property
    def is_empty(self):
        return not self

    @property
    def first(self):
        return self[0]

    @property
    def last(self):
        return self[-1]

    @property
    def is_sorted(self, key=lambda x: x):
        for i in range(len(self) - 1):
            if key(self[i]) > key(self[i + 1]):
                return False
        return True

    def push(self, element):
        return self.append(element)

    def for_each(self, callback):
        if not callable(callback):
            raise ValueError(f'Expected a function, got {callback} instead.')
        arg_count = len(inspect.getfullargspec(callback).args)
        for i, item in enumerate(self):
            arguments = []
            if arg_count >= 1:
                arguments.append(item)
            if arg_count >= 2:
                arguments.append(i)
            callback(*arguments)

    def map(self, callback):
        if not callable(callback):
            raise ValueError(f'Expected a function, got {callback} instead.')
        return MyList(map(callback, self))

    # Initialize n-dimensional list with
    # result of a lambda or just a value
    @classmethod
    def of(cls, size, value):
        if not isinstance(size, list):
            raise ValueError('Expected size to be a list of dimensions.')
        if len(size) == 0:
            raise ValueError('Size cannot be empty.')
        invalid_sizes_type = list(filter(lambda x: not isinstance(x, int), size))
        if len(invalid_sizes_type) > 0:
            raise ValueError('Sizes should be integers.')
        invalid_sizes_value = list(filter(lambda x: x <= 0, size))
        if len(invalid_sizes_value) > 0:
            raise ValueError('Sizes should be positive.')
        return MyList._of(size[::-1], value)

    @classmethod
    def _of(cls, size, value):
        if len(size) == 1:
            try:
                return MyList(value() for _ in range(size[0]))
            except TypeError:
                return MyList(value for _ in range(size[0]))
        else:
            count = size.pop()
            return MyList(
                MyList._of(size[:], value) for _ in range(count)
            )

    # overriding so that MyList is returned instead of list
    def copy(self):
        return MyList(list.copy(self))

    # overriding so that MyList is returned instead of list
    def __add__(self, other):
        return MyList(list.__add__(self, other))

    # overriding so that MyList is returned instead of list
    def __mul__(self, other):
        return MyList(list.__mul__(self, other))


class String(str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
   
    @property
    def length(self):
        return len(self)

    @property
    def is_empty(self):
        return not self

    @property
    def first(self):
        return self[0]

    @property
    def last(self):
        return self[-1]

    @property
    def is_sorted(self, key=lambda x: x):
        for i in range(len(self) - 1):
            if key(self[i]) > key(self[i + 1]):
                return False
        return True
    
    @classmethod
    def is_alphabet(cls, ch):
        return ch in String.alphabets


def solve(n, k, queries):
    this = This()

    remainder = 0

    for i, query in enumerate(queries, 1):
        remainder += query
        if remainder < k:
            print(i)
            return
        remainder -= k

    day = n + 1 + (remainder // k)

    print(day)


def main(*args):
    for _ in range(integer_input()):
        n, k = integer_array_input()
        q = integer_array_input()
        solve(n, k, q)


main()
