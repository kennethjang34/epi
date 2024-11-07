import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook


# TC: O(n*log(n)), SC: O(1)
# naive approach, as the solution doesn't have to involve sorting
def with_sorting(A: List[int]) -> None:
    A.sort()
    n = len(A)
    for i in range(1, n):
        if i & 1 == 1 and i != n - 1:
            A[i] = A[i + 1]


# TC: O(n), SC: O(1).
# intuition:
# Assume A[0:i] satisfies the question's condition.
# If i is even:
#   if A[i+1] >= A[i]: OK
#   else if A[i+1] < A[i]: swap A[i+1] and A[i]. This does not affect the previous A[0:i] elements' configuration, so we now have A[0:i+1] in valid configuration
# If i isoddeven:
#   if A[i+1] <= A[i]:  OK
#   else if A[i+1] > A[i]: swap A[i+1] and A[i]. This does not affect the previous A[0:i] elements' configuration, so we now have A[0:i+1] in valid configuration
def one_pass(A: List[int]) -> None:
    for i in range(len(A) - 1):
        a = A[i]
        b = A[i + 1]
        if a > b:
            if i & 1 == 0:
                A[i], A[i + 1] = b, a
        elif a < b:
            if i & 1 == 1:
                A[i], A[i + 1] = b, a


def rearrange(A: List[int]) -> None:
    # with_sorting(A)
    one_pass(A)


@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A
                    ).with_mismatch_info(
                        i,
                        "A[{}] <= A[{}]".format(i - 1, i),
                        "{} > {}".format(A[i - 1], A[i]),
                    )
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A
                        ).with_mismatch_info(
                            i,
                            "A[{}] >= A[{}]".format(i, i + 1),
                            "{} < {}".format(A[i], A[i + 1]),
                        )
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A
                        ).with_mismatch_info(
                            i,
                            "A[{}] >= A[{}]".format(i - 1, i),
                            "{} < {}".format(A[i - 1], A[i]),
                        )
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A
                        ).with_mismatch_info(
                            i,
                            "A[{}] <= A[{}]".format(i, i + 1),
                            "{} > {}".format(A[i], A[i + 1]),
                        )

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "alternating_array.py", "alternating_array.tsv", rearrange_wrapper
        )
    )
