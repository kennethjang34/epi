from test_framework import generic_test


def calculate(operator, n1, n2):
    if operator == "-":
        return n1 - n2
    if operator == "+":
        return n1 + n2
    if operator == "*":
        return n1 * n2
    if operator == "/":
        return n1 // n2


def is_int(token):
    return token.isdigit() or token.startswith("-") and token[1:].isdigit()


# TC: O(n)
def left_to_right(expression):
    tokens = expression.split(",")
    stk = []
    for token in tokens:
        if is_int(token=token):
            stk.append(int(token))
        else:
            n2 = stk.pop()
            n1 = stk.pop()
            stk.append(calculate(token, n1, n2))
    return stk[-1]



def evaluate(expression):
    return left_to_right(expression=expression)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", "evaluate_rpn.tsv", evaluate)
    )
