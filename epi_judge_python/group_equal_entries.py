import collections
import functools
from typing import DefaultDict, Dict, List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple("Person", ("age", "name"))


def group_by_age(people: List[Person]) -> None:
    # group_by_age_brute_force(people)
    # group_by_age_big_extra_space(people)
    group_by_age_opt(people)


# TC: O(n), SC: O(m), where n: input array size and m: distinct keys(ages)
# If age groups also need to be sorted, then use BST instead of regular dict for age_to_offset.
# If BST is used, TC will become O(n + m log m) as BST insertion takes O(log m)
def group_by_age_opt(people: List[Person]) -> None:
    age_to_count = collections.Counter((p.age for p in people))
    age_to_offset: Dict[int, int] = {}
    offset = 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count
    while len(age_to_offset) > 0:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]

        p = people[from_idx]
        to_age = p.age
        if p.age == from_age:
            age_to_offset[from_age] += 1
            age_to_count[from_age] -= 1
        else:
            to_idx = age_to_offset[to_age]
            people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
            age_to_offset[to_age] += 1
            age_to_count[to_age] -= 1

        if age_to_count[to_age] == 0:
            del age_to_count[to_age]
            del age_to_offset[to_age]


def group_by_age_big_extra_space(people: List[Person]) -> None:
    hm = DefaultDict(list)
    for p in people:
        hm[p.age].append(p)
    write_idx = 0
    for age_group in hm.values():
        for p in age_group:
            people[write_idx] = p
            write_idx += 1

    ## if needs to be sorted
    # ages = sorted(hm.keys())
    # cur_age_idx = 0
    # write_idx = 0
    #
    # while write_idx < len(people):
    #     age_group = hm[ages[cur_age_idx]]
    #     for p in age_group:
    #         people[write_idx] = p
    #         write_idx += 1
    #     cur_age_idx += 1


def group_by_age_brute_force(people: List[Person]) -> None:
    people.sort(key=lambda p: p.age)


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure("Empty result")

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure("Entry set changed")

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure("Entries are not grouped by age")
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "group_equal_entries.py", "group_equal_entries.tsv", group_by_age_wrapper
        )
    )
