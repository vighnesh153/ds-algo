class Array:
    @staticmethod
    def is_sorted(_array):
        for i in range(len(_array) - 1):
            if _array[i] > _array[i + 1]:
                return False
        return True


class Number:
    max = float('inf')
    min = -float('inf')


class This:
    def __init__(self):
        self.max = self.min = self.sum = self.count = None
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


class ListPlusPlus(list):
    def is_empty(self):
        return not self

    def last_index(self):
        return len(self) - 1

    # overriding so that list++ is returned instead of list
    def copy(self):
        return ListPlusPlus(list.copy(self))

    # overriding so that list++ is returned instead of list
    def __getitem__(self, item):
        return ListPlusPlus(list.__getitem__(self, item))

    # overriding so that list++ is returned instead of list
    def __add__(self, other):
        return ListPlusPlus(list.__add__(self, other))

    # overriding so that list++ is returned instead of list
    def __mul__(self, other):
        return ListPlusPlus(list.__mul__(self, other))


def get_total_subarrays(arr):
    n = len(arr)
    return n * (n + 1) // 2


def solve(arr, k):
    this = This()

    # Write your code below this comment
    i = j = 0
    product = arr[i]
    while j < len(arr):
        if product >= k:
            this.count += len(arr) - j
            product //= arr[i] if i < len(arr) else 1
            i += 1
        else:
            j += 1
            product *= arr[j] if j < len(arr) else 1
        if i > j:
            j = i
            product *= arr[j] if j < len(arr) else 1

    total_sub_arrays = get_total_subarrays(arr)
    return total_sub_arrays - this.count


def main(*args):
    # do initialization and initial transformations
    # here if needed so that solve() stays clean
    return solve(*args)


inputs = [
    [1, 2, 3],
    0
]
print(main(*inputs))
