from test_framework import generic_test
from test_framework.test_failure import TestFailure


class LruCache:
    class Book:
        def __init__(self, isbn, price) -> None:
            self.isbn = isbn
            self.price = price
            self.prev = None
            self.next = None

        def __repr__(self) -> str:
            return f"isbn: {self.isbn}, price: {self.price}"

    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity
        self.lru_head = LruCache.Book(-1, -1)
        self.lru_tail = LruCache.Book(-1, -1)
        self.lru_head.next = self.lru_tail
        self.lru_tail.prev = self.lru_head

    def __update_lru(self, book):
        book.prev.next = book.next
        book.next.prev = book.prev
        book.prev = self.lru_tail.prev
        book.prev.next = book
        book.next = self.lru_tail
        self.lru_tail.prev = book

    def lookup(self, isbn: int) -> int:
        if isbn in self.cache:
            book = self.cache[isbn]
            self.__update_lru(book)
            return book.price
        else:
            return -1

    def insert(self, isbn: int, price: int) -> None:
        if isbn not in self.cache:
            book = LruCache.Book(isbn, price)
            if len(self.cache) < self.capacity:
                self.lru_tail.prev.next = book
                book.prev = self.lru_tail.prev
                book.next = self.lru_tail
                self.lru_tail.prev = book
                self.cache[isbn] = book
            else:
                self.erase(self.lru_head.next.isbn)
                self.lru_tail.prev.next = book
                book.prev = self.lru_tail.prev
                book.next = self.lru_tail
                self.lru_tail.prev = book
                self.cache[isbn] = book
        else:
            self.__update_lru(self.cache[isbn])

    def erase(self, isbn: int) -> bool:
        if isbn in self.cache:
            book = self.cache[isbn]
            book.prev.next = book.next
            book.next.prev = book.prev
            del self.cache[isbn]
            return True
        else:
            return False

    def print_lru(self):
        node = self.lru_head
        while node is not None:
            print(node, "->")
            node = node.next


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != "LruCache":
        raise RuntimeError("Expected LruCache as first command")

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == "lookup":
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    "Lookup: expected " + str(cmd[2]) + ", got " + str(result)
                )
        elif cmd[0] == "insert":
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == "erase":
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    "Erase: expected " + str(cmd[2]) + ", got " + str(result)
                )
        else:
            raise RuntimeError("Unexpected command " + cmd[0])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lru_cache.py", "lru_cache.tsv", lru_cache_tester
        )
    )
