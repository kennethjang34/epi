from test_framework import generic_test
from test_framework.test_failure import TestFailure

import math
import collections


class BruteForceCircularQueueWithMax:
    def __init__(self) -> None:
        self._inner = [0]
        self._head = 0
        self._tail = 0
        self._num_elements = 0

    # O(1) amortized
    def enqueue(self, x: int) -> None:
        if self._num_elements >= len(self._inner):
            self._inner, self._head, self._tail = (
                (
                    self._inner[self._head :]
                    + self._inner[: self._head]
                    + [0] * len(self._inner)
                ),
                0,
                len(self._inner),
            )
        self._inner[self._tail] = x
        self._tail = (self._tail + 1) % len(self._inner)
        self._num_elements += 1

    # O(1)
    def dequeue(self) -> int:
        val = self._inner[self._head]
        self._head = (self._head + 1) % len(self._inner)
        self._num_elements -= 1
        return val

    # O(n)
    def max(self) -> int:
        max_v = -math.inf
        start = self._head
        end = self._tail if self._tail > self._head else self._tail + len(self._inner)
        for i in range(start, end):
            v = self._inner[i % len(self._inner)]
            max_v = max(v, max_v)
        return int(max_v)


class OptimizedQueueWithMax:
    def __init__(self) -> None:
        self._inner = collections.deque()
        self._maxes = collections.deque()

    # TC: O(n) in the worst case, but O(1) amortized because m operations of enqueueing and dequeueing will have O(m)
    # since each element is popped at most once in self._inner and self._max
    def enqueue(self, x: int) -> None:
        self._inner.append(x)
        count = 1
        if len(self._maxes) == 0:
            self._maxes.append([x, 1])
        else:
            last_max = self._maxes[-1]
            while len(self._maxes) > 0 and self._maxes[-1][0] <= x:
                last_max = self._maxes[-1]
                if last_max[0] == x:
                    count += 1
                self._maxes.pop()
            self._maxes.append([x, count])

    # TC: O(1)
    def dequeue(self) -> int:
        val = self._inner.popleft()
        if val == self._maxes[0][0]:
            self._maxes[0][1] -= 1
            if self._maxes[0][1] == 0:
                self._maxes.popleft()
        return val

    # O(1)
    def max(self) -> int:
        return self._maxes[0][0]


# QueueWithMax = BruteForceCircularQueueWithMax
QueueWithMax = OptimizedQueueWithMax


def queue_tester(ops):
    try:
        q = QueueWithMax()

        for op, arg in ops:
            if op == "QueueWithMax":
                q = QueueWithMax()
            elif op == "enqueue":
                q.enqueue(arg)
            elif op == "dequeue":
                result = q.dequeue()
                if result != arg:
                    raise TestFailure(
                        "Dequeue: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "queue_with_max.py", "queue_with_max.tsv", queue_tester
        )
    )
