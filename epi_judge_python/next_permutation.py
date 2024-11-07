from math import inf
from typing import List

from test_framework import generic_test


# TC: O(n), SC: O(1)
# intuition: permutation in which ith element is not greather than i+1th element (e.g. in the decreasing order) is the biggest out of all the permutation obtainable from arranging its elements
# ex: there is no such permutatino that is bigger than (5,4,3,2,1) itself
# if permutation is (a1,a2,a3,b1,b2,b3), where b1 >= b2 >= b3 and a3 < b1, the next biggest permutation could be obtained by modifying sub arry: (a3,b1,b2,b3)
# let suffix be (b1,b2,b3). find the smallest element in the suffix that's still bigger than a3. such a3 is guaranteed to exist.
# let that element be b2. then by swapping b2 and a3, we get b2, (b1,a3,b3). 
# we now have a new suffix (b1,a3,b3), but the suffix doesn't have to be the smallest possible permutation that can be obtained arranging b1,a3,b3. However, the suffix is still in decreasing order so
# they are rather the biggest permutation. By reversing the suffix, we get (b3,a3,b1), which is in the increasing order. This means they are the smallest permutation possible of the suffix.
# so now we have a1,a2,b2,b3,a3,b1, which is the next biggest permutation
def next_permutation(perm: List[int]) -> List[int]:
    n = len(perm)
    prev = None
    prev = perm[-1]
    for i in range(n - 2, -1, -1):
        if perm[i] >= prev:
            prev = perm[i]
        else:
            e = perm[i]
            for idx in range(n - 1, i, -1):
                s = perm[idx]
                if s > e:
                    perm[idx] = e
                    perm[i] = s
                    perm[i + 1 :] = reversed(perm[i + 1 :])
                    return perm
    return []


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", "next_permutation.tsv", next_permutation
        )
    )
