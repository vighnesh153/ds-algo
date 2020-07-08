# Problem:
# https://www.codechef.com/JULY20B/problems/PTMSSNG


import inspect


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


def solve(points):
    this = This()

    # Write your code below this comment

    from collections import defaultdict

    x_values = defaultdict(lambda: 0)
    y_values = defaultdict(lambda: 0)

    for x, y in points:
        x_values[x] += 1
        y_values[y] += 1

    x = y = None

    for key, count in x_values.items():
        if count % 2 == 1:
            x = key
            break

    for key, count in y_values.items():
        if count % 2 == 1:
            y = key
            break

    print(x, y)


def main(*args):
    # do initialization and initial transformations
    # here if needed so that solve() stays clean

    for _ in range(Input.integer()):
        points = MyList()
        for _ in range(4 * Input.integer() - 1):
            points.push(Input.array_integer())
        solve(points)


main()
