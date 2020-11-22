# Problem: https://www.codechef.com/NOV20B/problems/FEMA2
# Editorial: https://discuss.codechef.com/t/fema2-editorial/79956

import inspect
import sys


Infinity = float('inf')

# Default is around 1000
sys.setrecursionlimit(110000)


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


def pre_process(s):
    characters = MyList()
    for ch in s:
        if ch == ":":
            characters.append("_")
            characters.append("_")
        else:
            characters.append(ch)
    return characters


def in_range(i, j, k):
    return k + 1 - abs(i - j) > 0


def is_magnet(characters, i):
    return characters[i] == "M"


def is_iron(characters, i):
    return characters[i] == "I"


def solve(s, k):
    this = This()
    characters = pre_process(s)
    i, j = 0, 0
    while i < characters.length and j < characters.length:
        if is_magnet(characters, i):
            if is_iron(characters, j):
                if in_range(i, j, k):
                    this.count += 1

                    # current magnet already counted
                    i += 1

                elif j > i:
                    # this magnet can't have any pair with iron
                    i += 1

                    # don't skip the current iron. To nullify the effect on next line
                    j -= 1

            j += 1
        else:
            i += 1

    return this.count


def main(*args):
    for _ in test_case_count():
        n, k = integer_array_input()
        s = string_input()
        strings = s.split("X")
        print(sum(solve(sub_str, k) for sub_str in strings))


main()
