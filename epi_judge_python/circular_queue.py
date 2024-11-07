from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.head = 0
        # self.tail represents the end of the queue, exclusively.
        # if self.head < self.tail, then queue is self.inner[self.head:self.tail]
        # the reason why the initial value is None is to distinguish between queue of length 0 vs queue of length equal to its current max capacity
        self.tail = None
        self.inner = [0] * capacity
        return

    # TC(amortized): O(1)
    def enqueue(self, x: int) -> None:
        if self.tail is None:
            self.tail = self.head
        elif self.tail == self.head:
            self.inner[:] = self.inner[self.head :] + self.inner[: self.head]
            self.head = 0
            self.tail = len(self.inner)
            self.inner = [v for v in self.inner] + [0] * len(self.inner)
        self.inner[self.tail] = x
        self.tail = (self.tail + 1) % len(self.inner)
        return

    # TC: O(1)
    def dequeue(self) -> int:
        if self.tail is None:
            raise IndexError
        val = self.inner[self.head]
        self.head = (self.head + 1) % len(self.inner)
        if self.head == self.tail:
            self.tail = None
        return val

    # TC: O(1)
    def size(self) -> int:
        if self.tail is None:
            return 0
        if self.tail == self.head:
            return len(self.inner)
        return (self.tail - self.head) % len(self.inner)


def queue_tester(ops):
    q = Queue(1)

    for op, arg in ops:
        if op == "Queue":
            q = Queue(arg)
        elif op == "enqueue":
            q.enqueue(arg)
        elif op == "dequeue":
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result)
                )
        elif op == "size":
            result = q.size()
            if result != arg:
                raise TestFailure("Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "circular_queue.py", "circular_queue.tsv", queue_tester
        )
    )
