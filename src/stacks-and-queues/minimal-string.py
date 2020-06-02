# https://codeforces.com/contest/797/problem/C

import inspect
from collections import Counter


class Input:
    @classmethod
    def array_integer(cls):
        return MyList(map(int, input().split()))
    
    @classmethod
    def array_string(cls):
        return input().split()

    @classmethod
    def integer(cls):
        return int(input())
    
    @classmethod
    def float(cls):
        return float(input())
    
    @classmethod
    def string(cls):
        return input()


class Number:
    max = float('inf')
    min = -float('inf')

    @classmethod
    def is_digit(cls, character):
        return character in "0123456789"


class This:
    def __init__(self):
        self.max = self.min = self.sum = self.count = None
        self.set = set()
        self.map = dict()
        self.reset()

    def update_if_max(self, value):
        self.max = max(self.max, value)

    def update_if_min(self, value):
        self.min = min(self.min, value)

    def reset(self):
        self.min = Number.max
        self.max = Number.min
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
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    @classmethod
    def is_alphabet(cls, ch):
        return ch in String.alphabets


def solve():
    s = Input.string()
    s = MyList(s[::-1])

    counter = Counter(s)
    counter = [counter.get(ch, 0) for ch in String.alphabets]

    def get_lowest():
        index = -1
        for i, num in enumerate(counter):
            if num != 0:
                index = i
                break

        return chr(ord('a') + index)

    def decrement(ch):
        index = ord(ch) - ord('a')
        counter[index] -= 1

    temp = MyList()
    final = MyList()

    while not s.is_empty:
        item = s.pop()
        lowest = get_lowest()
        while not temp.is_empty:
            if temp.last == lowest:
                final.push(temp.pop())
                decrement(lowest)
            else:
                break
            lowest = get_lowest()
        if item == lowest:
            final.push(item)
        else:
            temp.push(item)
        decrement(item)

    while not temp.is_empty:
        final.push(temp.pop())

    print(''.join(final))


solve()
