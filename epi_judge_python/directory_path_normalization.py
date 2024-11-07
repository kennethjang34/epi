from test_framework import generic_test

# TC: O(n)
def shortest_equivalent_path(path: str) -> str:
    if len(path) == 0:
        raise ValueError("Empty path")
    stk = []
    if path[0] == "/":
        stk.append("")
        path = path[1:]
    elif len(path) >= 2 and path[0:2] == "./":
        path = path[2:]
    parsed = path.split("/")
    for token in parsed:
        if token == "" or token == ".":
            continue
        if token == "..":
            if len(stk) == 0 or stk[-1] == "..":
                stk.append(token)
            elif stk[-1] == "":
                raise ValueError("Path Error")
            else:
                stk.pop()
        else:
            stk.append(token)
    if len(stk) == 1 and stk[0] == "":
        return "/"
    return "/".join(stk)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "directory_path_normalization.py",
            "directory_path_normalization.tsv",
            shortest_equivalent_path,
        )
    )
