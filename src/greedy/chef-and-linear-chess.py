# https://www.codechef.com/AUG20B/problems/LINCHESS
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


def solve(n, k, places):
    this = This()

    # Write your code below this comment
    smallest = None
    count = Number.max
    for i in places:
        if i > k:
            continue
        if i == k:
            print(0)
            return
        if k % i == 0:
            c = k // i
            if c < count:
                count = c
                smallest = i

    print(-1 if smallest is None else smallest)


def main(*args):
    # do initialization and initial transformations
    # here if needed so that solve() stays clean
    for _ in range(Input.integer()):
        n, k = Input.array_integer()
        places = Input.array_integer()
        solve(n, k, places)


main()
