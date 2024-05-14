from typing import List


def to_dict(data: List[list]):
    return [{f'k{i + 1}': v for i, v in enumerate(item)} for item in data]


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
    assert to_dict(a) == b, to_dict(a)
