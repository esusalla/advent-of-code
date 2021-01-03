# Day 18, Part 1: Operation Order

import collections


def find_match(expr):
    stack = collections.deque()

    idx = expr.index("(")
    for i, x in enumerate(expr):
        if x == "(":
            stack.appendleft((i, x))

        elif x == ")":
            stack.popleft()
            if not stack:
                return idx, i


def evaluate(expr):
    if "(" in expr:
        start, end = find_match(expr)
        val = evaluate(expr[start+1:end])
        return evaluate(expr[:start] + [str(val)] + expr[end+1:])

    while len(expr) > 1:
        expr = [str(eval(" ".join(expr[:3])))] + expr[3:]
    return expr[0]


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    EXPRS = [list(line.replace(" ", "")) for line in INP.split("\n")]

    total = sum(int(evaluate(expr)) for expr in EXPRS)
    print(total)
