# Problem statement
# https://www.codechef.com/JULY20B/problems/DRCHEF

import inspect
from heapq import *


class Input:
    @classmethod
    def array_integer(cls):
        return MyList(map(int, input().split()))

    @classmethod
    def array_string(cls):
        return MyList(map(String, input().split()))

    @classmethod
    def integer(cls):
        return int(input())

    @classmethod
    def float(cls):
        return float(input())

    @classmethod
    def string(cls):
        return String(input())


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

    def update_if_max(self, *values):
        self.max = max(self.max, *values)

    def update_if_min(self, *values):
        self.min = min(self.min, *values)

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


def solve(arr, x, mandatory_days):
    permanent_arr = arr.copy()
    arr = MyList([arr[i], i] for i in range(arr.length))
    heapify(arr)

    days = 0
    cures = x
    while arr.length > 0:
        top = heappop(arr)
        delivered = min(cures, permanent_arr[top[1]])
        left = top[0] - delivered
        top[0] = min(permanent_arr[top[1]], left * 2)
        if top[0] > 0:
            heappush(arr, top)
        cures = delivered * 2
        days += 1

    print(days + mandatory_days)


def main(*args):
    for _ in range(Input.integer()):
        n, x = Input.array_integer()
        to_be_passed = MyList()
        mandatory_days = 0
        is_cure_count_present = False
        max_less_than = 0
        for elem in Input.array_integer():
            if elem >= x:
                if elem == x:
                    is_cure_count_present = True
                to_be_passed.push(elem)
            else:
                mandatory_days += 1
                max_less_than = max(max_less_than, elem)
        if not is_cure_count_present and max_less_than * 2 > x:
            to_be_passed.push(max_less_than)
            mandatory_days -= 1
        solve(to_be_passed, x, mandatory_days)


main()
