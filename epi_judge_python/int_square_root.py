from test_framework import generic_test


# TC: O(log n)
# def square_root_v1(k: int) -> int:
#     l = 0
#     r = k
#     while l <= r:
#         mid = l + (r - l) // 2
#         squared = mid**2
#         if squared > k:
#             r = mid - 1
#         elif squared < k:
#             l = mid + 1
#         else:
#             return mid
#     return l - 1
def square_root(k: int) -> int:
    l = 0
    r = k
    while True:
        mid = l + (r - l) // 2
        squared = mid**2
        if r == l:
            if squared > k:
                l -= 1
                break
            else:
                return mid
        else:
            if squared > k:
                r = mid
            else:
                l = mid + 1
    return l


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_square_root.py", "int_square_root.tsv", square_root
        )
    )
