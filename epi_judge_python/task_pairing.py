import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple("PairedTasks", ("task_1", "task_2"))


# TC: O(n log n)
def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    sorted_tasks = sorted(task_durations)
    pairs = []
    for i in range(len(sorted_tasks) // 2):
        pairs.append(
            PairedTasks(sorted_tasks[i], sorted_tasks[len(sorted_tasks) - 1 - i])
        )
    return pairs


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "task_pairing.py", "task_pairing.tsv", optimum_task_assignment
        )
    )
