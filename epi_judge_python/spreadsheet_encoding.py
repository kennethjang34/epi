from test_framework import generic_test


# TC: O(n), n: len(col)
def ss_decode_col_id(col: str) -> int:
    int_id = 0
    for c in col:
        int_id = int_id * 26 + ord(c) - ord("A") + 1
    # for testing ss_encoding_col_id
    # col = ss_encode_col_id(int_id)
    # print()
    # print(
    #     "original col",
    #     col,
    #     "corresponding int_id",
    #     int_id,
    # )
    # print(
    #     "returned by ss_encode_col_id",
    #     col,
    # )
    # int_id = 0
    # for c in col:
    #     int_id = int_id * 26 + ord(c) - ord("A") + 1

    return int_id

# TC: O(n), n: len(col)
def ss_encode_col_id(int_id: int) -> str:
    if int_id == 0:
        return ""
    col = []
    while int_id > 0:
        next = int_id % 26
        int_id //= 26
        if next == 26:
            col.append("Z")
        else:
            col.append(chr(ord("A") + next - 1))
    return "".join(reversed(col))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spreadsheet_encoding.py", "spreadsheet_encoding.tsv", ss_decode_col_id
        )
    )
