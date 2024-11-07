from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.inner = []

    def push(self, x):
        self.inner.append(x)

    def pop(self):
        return self.inner.pop()

    def size(self):
        return len(self.inner)


# very slow dequeueing as it constructs two temporary stacks with separate traversal
# NOTE: This approach takes O(m^2) time for m operations because ith element is pushed and popped 2*(i-1) times
class BruteForceQueueWithStack:
    def __init__(self) -> None:
        self.inner = Stack()

    # TC: O(1)
    def enqueue(self, x: int) -> None:
        self.inner.push(x)

    # TC: O(n)
    def dequeue(self) -> int:
        new_stk = Stack()
        while self.inner.size() > 0:
            new_stk.push(self.inner.pop())
        self.inner = Stack()
        to_return = new_stk.pop()
        while new_stk.size() > 0:
            self.inner.push(new_stk.pop())
        return to_return


# faster than brute force approach because we only construct a new stack when the existing stack for dequeueing is empty
# NOTE: This approach takes O(m) time for m operations because each element is pushed no more than twice and popped no more than twice
class QueueWithTwoStacks:
    def __init__(self) -> None:
        self._enq = Stack()
        self._deq = Stack()

    # TC: O(1)
    def enqueue(self, x: int) -> None:
        self._enq.push(x)

    # TC: O(n) in worst case, O(1) amortized
    def dequeue(self) -> int:
        if self._deq.size() == 0:
            while self._enq.size() > 0:
                self._deq.push(self._enq.pop())
        return self._deq.pop()


Queue = QueueWithTwoStacks


def queue_tester(ops):
    try:
        q = Queue()

        for op, arg in ops:
            if op == "Queue":
                q = Queue()
            elif op == "enqueue":
                q.enqueue(arg)
            elif op == "dequeue":
                result = q.dequeue()
                if result != arg:
                    raise TestFailure(
                        "Dequeue: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "queue_from_stacks.py", "queue_from_stacks.tsv", queue_tester
        )
    )
