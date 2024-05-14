from typing import List, Tuple
from functools import reduce


def count(data: List[set]) -> int:
    return len(reduce(lambda s1, s2: s1.union(s2), data))


def _sum(data: List[set]) -> int:
    return sum([sum(s) for s in data])


def mean(data: List[set]) -> float:
    return _sum(data) / count(data)


def main(data: List[set]) -> Tuple[int, int, float]:
    data_count = count(data)
    data_sum = _sum(data)
    data_mean = mean(data)
    return data_count, data_sum, data_mean


if __name__ == '__main__':
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
    cnt, s, mn = main(m)
    print(f'count: {cnt}')
    print(f'sum: {s}')
    print(f'mean: {mn}')
