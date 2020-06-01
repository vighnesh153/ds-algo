from bisect import bisect, insort


class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        new_interval = [start, end]

        if len(self.events) == 0:
            self.events.append(new_interval)
            return True

        index = bisect(self.events, new_interval)

        if index == len(self.events):
            if start >= self.events[-1][1]:
                self.events.append(new_interval)
                return True
            return False

        if index == 0:
            if end <= self.events[0]:
                insort(self.events, new_interval)
                return True
            return False

        if start < self.events[index - 1][1]:
            return False

        if end > self.events[index][0]:
            return False

        insort(self.events, new_interval)
        return True


obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))
