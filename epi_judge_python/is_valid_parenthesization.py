from test_framework import generic_test


def is_opening_bracket(b) -> bool:
    if b is None or b not in ("(", "{", "["):
        return False
    return True


def is_closing_bracket(b) -> bool:
    if b is None or b not in (")", "}", "]"):
        return False
    return True


def is_match(a, b) -> bool:
    if a == "(" and b == ")":
        return True
    if a == "{" and b == "}":
        return True
    if a == "[" and b == "]":
        return True
    return False


# TC: O(n)
def is_well_formed(s: str) -> bool:
    stk = []
    i = 0
    while i < len(s):
        c = s[i]
        if is_opening_bracket(c):
            stk.append(c)
        elif is_closing_bracket(c):
            if len(stk) == 0:
                return False
            prev = stk.pop()
            if not is_match(prev, c):
                return False
        i += 1
    return len(stk) == 0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_parenthesization.py",
            "is_valid_parenthesization.tsv",
            is_well_formed,
        )
    )
