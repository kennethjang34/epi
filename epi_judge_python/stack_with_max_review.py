from test_framework import generic_test
from test_framework.test_failure import TestFailure
import heapq
import collections


# SC: O(n)
class StackWithHeap:
    # TC: O(1)
    def __init__(self):
        self.inner = []
        self.encountered = {}
        self.max_val = []

    # TC: O(n)
    def empty(self) -> bool:
        return len(self.inner) == 0

    # TC: most of the time O(log(n)) but in worst case: O(n* log(n))
    def max(self) -> int:
        if len(self.inner) == 0:
            raise AssertionError("stack empty")
        x = -heapq.heappop(self.max_val)
        while self.encountered[x] == 0:
            x = -heapq.heappop(self.max_val)
        heapq.heappush(self.max_val, -x)
        return x

    # TC: O(1)
    def pop(self) -> int:
        if len(self.inner) == 0:
            raise AssertionError("stack empty")
        val = self.inner.pop()
        self.encountered[val] -= 1
        return val

    # TC: O(log(n))
    def push(self, x: int) -> None:
        self.inner.append(x)
        if self.encountered.setdefault(x, 0) == 0:
            heapq.heappush(self.max_val, -x)
        self.encountered[x] += 1


# SC: O(n)
class StackWithCaching:
    ElementWithCachedMax = collections.namedtuple(
        "ElementWithCachedMax", ("val", "max_cache")
    )

    # TC: O(1)
    def __init__(self):
        self.inner = []

    # TC: O(1)
    def empty(self) -> bool:
        return len(self.inner) == 0

    # TC: O(1)
    def max(self) -> int:
        if len(self.inner) == 0:
            raise AssertionError("stack empty")
        return self.inner[-1].max_cache

    # TC: O(1)
    def pop(self) -> int:
        if len(self.inner) == 0:
            raise AssertionError("stack empty")
        return self.inner.pop().val

    # TC: O(1)
    def push(self, x: int) -> None:
        self.inner.append(
            StackWithCaching.ElementWithCachedMax(
                x, x if len(self.inner) == 0 else max(self.max(), x)
            )
        )


# SC: O(n)
# almost the same logic as StackWithCaching impl, but instead of adding max_caching to every element, keep track of current max value and its number of encounter
# so that if max value is not changing with newly pushed value, we don't have to use additional space pointlessly
class StackWithCachingSpaceOptimized:
    # TC: O(1)
    def __init__(self):
        self.inner = []
        self.max_val = []

    # TC: O(n)
    def empty(self) -> bool:
        return len(self.inner) == 0

    # TC: most of the time O(log(n)) but in worst case: O(n* log(n))
    def max(self) -> int:
        if len(self.inner) == 0:
            raise AssertionError("stack empty")
        x = self.max_val[-1]
        return x[0]

    # TC: O(1)
    def pop(self) -> int:
        if len(self.inner) == 0:
            raise AssertionError("stack empty")
        val = self.inner.pop()
        if val == self.max_val[-1][0]:
            self.max_val[-1][1] -= 1
            if self.max_val[-1][1] == 0:
                self.max_val.pop()
        return val

    # TC: O(log(n))
    def push(self, x: int) -> None:
        self.inner.append(x)
        if len(self.max_val) == 0 or x > self.max_val[-1][0]:
            self.max_val.append([x, 1])
        else:
            if x == self.max_val[-1][0]:
                self.max_val[-1][1] += 1


# Stack = StackWithHeap
# Stack = StackWithCaching
Stack = StackWithCachingSpaceOptimized


def stack_tester(ops):
    try:
        s = Stack()

        for op, arg in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
