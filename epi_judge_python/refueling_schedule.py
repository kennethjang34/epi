import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    # return find_ample_city_bf(gallons, distances, MPG)
    return find_ample_city_optimal(gallons, distances, MPG)


# TC: O(n)
def find_ample_city_optimal(gallons: List[int], distances: List[int], mpg: int) -> int:
    ample = None
    num_cities = len(gallons)
    i = 0
    while i < num_cities:
        if gallons[i] < distances[i] / mpg:
            i += 1
            continue
        gas = gallons[i] - (distances[i] / mpg)
        j = i + 1
        while gas >= 0 and j < i + num_cities:
            city = j % num_cities
            gas_needed = distances[city] / mpg
            gas_refill = gallons[city]
            gas = gas - gas_needed + gas_refill
            j += 1
        if j == i + num_cities:
            ample = i
            break
        else:
            i = j
    return ample

# TC: O(n^2)
def find_ample_city_bf(gallons: List[int], distances: List[int], mpg: int) -> int:
    ample = None
    for i in range(len(gallons)):
        gas = gallons[i]
        j = i
        while gas >= (distances[(j) % len(gallons)] / mpg) and j < i + len(gallons):
            city = j % len(gallons)
            gas_needed = distances[city] / mpg
            gas_refill = gallons[(j + 1) % len(gallons)]
            gas = gas - gas_needed + gas_refill
            j += 1
        if j == i + len(gallons):
            ample = i
            break
    return ample


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure("Out of gas on city {}".format(i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "refueling_schedule.py", "refueling_schedule.tsv", find_ample_city_wrapper
        )
    )
