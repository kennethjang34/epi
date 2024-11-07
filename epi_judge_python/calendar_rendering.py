import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from heapq import *

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple("Event", ("start", "finish"))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # return find_max_simultaneous_events_with_priority_q(A)
    return find_max_simultaneous_events_with_distinguished_endpoints(A)


# TC: O(n log n)
def find_max_simultaneous_events_with_distinguished_endpoints(A: List[Event]) -> int:
    Endpoint = collections.namedtuple("Endpoint", ("time", "is_start"))

    endpoints = [
        p
        for event in A
        for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
    ]
    # If two endpoints have the same time, then starting point must come first
    # as intervals include the finish point as well, so they can qualify for 'overlapping'
    endpoints.sort(key=lambda p: (p.time, not p.is_start))
    max_count = 0
    cur_count = 0
    for endpoint in endpoints:
        if endpoint.is_start:
            cur_count += 1
            max_count = max(max_count, cur_count)
        else:
            cur_count -= 1
    return max_count


# TC: O(n log n)
def find_max_simultaneous_events_with_priority_q(A: List[Event]) -> int:
    sorted_A = sorted(A, key=lambda e: e.start)
    max_count = 0
    hp = []

    def event_lt(self, other):
        return self.finish < other.finish

    Event.__lt__ = event_lt
    for e in sorted_A:
        while len(hp) > 0 and hp[0].finish < e.start:
            heappop(hp)
        heappush(hp, e)
        max_count = max(max_count, len(hp))
    return max_count


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events, events))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "calendar_rendering.py",
            "calendar_rendering.tsv",
            find_max_simultaneous_events_wrapper,
        )
    )
