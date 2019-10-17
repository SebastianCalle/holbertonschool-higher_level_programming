#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Print pascal triangle"""
    line = []
    if n > 0:
        line.append([1])
        for j in range(0, n - 1):
            i = -1
            op = []
            while i < len(line[j]) - 1:
                if i == -1:
                    op.append(1)
                else:
                    op.append(line[j][i] +
                              line[j][i + 1])
                i += 1
            op.append(1)
            line.append(op)
    return line
