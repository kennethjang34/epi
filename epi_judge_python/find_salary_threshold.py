from typing import List

from test_framework import generic_test
from math import isclose


# TC: O(n log n)
def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    avg = target_payroll / len(current_salaries)
    threshold = avg
    for i, salary in enumerate(current_salaries):
        if isclose(salary, threshold):
            return threshold
        if salary < threshold:
            if i == len(current_salaries) - 1:
                return -1
            threshold = threshold + (
                (threshold - salary) / (len(current_salaries) - (i + 1))
            )
        else:
            break
    return threshold


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "find_salary_threshold.py", "find_salary_threshold.tsv", find_salary_cap
        )
    )
