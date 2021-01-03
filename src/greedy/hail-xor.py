# https://www.codechef.com/DEC20B/problems/HXOR

import inspect
import sys

from typing import List, Tuple

from heapq import *


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


def is_odd(n):
    return n % 2 == 1


def is_even(n):
    return n % 2 == 0


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


max_bits = 30


def convert_to_binary(arr):
    binary = []
    for el in arr:
        b = bin(el)[2:].zfill(max_bits)
        binary.append(list(b))
    return binary


def get_indices(binary):
    indices = [[] for _ in range(max_bits)]
    for j, item in enumerate(binary):
        for i, el in enumerate(item):
            if el == "1":
                indices[i].append(j)
    return indices


def custom_heapify(indices):
    pre_processing = []
    for i, item in enumerate(indices):
        if len(item) > 0:
            pre_processing.append((item[0], i, item[::-1]))

    heapify(pre_processing)
    return pre_processing


def solve(n, x, arr):
    # Write your code below this comment

    binary: List[List[str]] = convert_to_binary(arr)
    indices = get_indices(binary)
    heap: List[Tuple[int, int, List]] = custom_heapify(indices)

    c = 1
    while heap and c <= x:
        _, column, item = heappop(heap)
        if len(item) >= 2:
            i = item.pop()
            j = item.pop()
            binary[i][column] = "0"
            binary[j][column] = "0"
            if len(item) > 0:
                heappush(heap, (item[-1], column, item))
        elif len(item) == 1:
            i = item.pop()
            if i == n - 1:
                continue
            binary[i][column] = "0"
            binary[n - 1][column] = "1"
        c += 1

    decimal = []
    for b in binary:
        decimal.append(int("".join(b), 2))

    print(*decimal)


def main():
    # do initialization and initial transformations
    # here if needed so that solve() stays clean

    for _ in test_case_count():
        n, x = integer_array_input()
        arr = integer_array_input()
        solve(n, x, arr)


main()


def test_convert_to_binary():
    arr = [2, 3, 4, 5, 10, 5, 13]

    global max_bits
    max_bits = 5

    binary = convert_to_binary(arr)
    expected = [
        ["0", "0", "0", "1", "0"],
        ["0", "0", "0", "1", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
        ["0", "0", "1", "0", "1"],
        ["0", "1", "1", "0", "1"],
    ]

    print("Test Convert to Binary:", "PASSED" if binary == expected else "FAILED")
    if binary != expected:
        print("*" * 40)
        print(binary)
        print(expected)
        print("*" * 40)


def test_get_indices():
    arr = [2, 3, 4, 5, 10, 5, 13]

    global max_bits
    max_bits = 5

    binary = convert_to_binary(arr)

    indices = get_indices(binary)
    expected = [[], [4, 6], [2, 3, 5, 6], [0, 1, 4], [1, 3, 5, 6]]

    print("Test Get Indices:", "PASSED" if indices == expected else "FAILED")
    if indices != expected:
        print("*" * 40)
        print(indices)
        print(expected)
        print("*" * 40)


def test_custom_heapify():
    arr = [2, 3, 4, 5, 10, 5, 13]

    global max_bits
    max_bits = 5

    binary = convert_to_binary(arr)
    indices = get_indices(binary)
    heap = custom_heapify(indices)

    first, column, item = heappop(heap)
    if first != 0 or column != 3 or item != [4, 1, 0]:
        print("Test Custom Heapify: FAILED")
        return
    heappush(heap, (4, column, [4]))

    first, column, item = heappop(heap)
    if first != 1 or column != 4 or item != [6, 5, 3, 1]:
        print("Test Custom Heapify: FAILED")
        return
    heappush(heap, (5, column, [6, 5]))

    first, column, item = heappop(heap)
    if first != 2 or column != 2 or item != [6, 5, 3, 2]:
        print("Test Custom Heapify: FAILED")
        return
    heappush(heap, (5, column, [6, 5]))

    first, column, item = heappop(heap)
    if first != 4 or column != 1 or item != [6, 4]:
        print("Test Custom Heapify: FAILED")
        return

    first, column, item = heappop(heap)
    if first != 4 or column != 3 or item != [4]:
        print("Test Custom Heapify: FAILED")
        return

    first, column, item = heappop(heap)
    if first != 5 or column != 2 or item != [6, 5]:
        print("Test Custom Heapify: FAILED")
        return

    first, column, item = heappop(heap)
    if first != 5 or column != 4 or item != [6, 5]:
        print("Test Custom Heapify: FAILED")
        return

    if len(heap) != 0:
        print("Test Custom Heapify: FAILED")

    print("Test Custom Heapify: PASSED")


def tests():
    test_convert_to_binary()
    test_get_indices()
    test_custom_heapify()


# tests()
