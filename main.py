import time
from typing import Dict, Iterable
"""

First: Run the following code using Python7+ (otherwise the type hints
will throw an error)

Second: Figure out what the function `solution` is doing

Third: Optimize the function `solution` to run under 2 seconds.
It is possible to run under a second.

### 
Addition:
Optimize work with memory:
1) reading data from file
* sys.getsizeof(fixed_arr) == 83120 # bytes
2) storing data
    standard dict:
        sys.getsizeof({"first": 1, "last": 22}) == 248 # bytes
    the Pair class:
        sys.getsizeof(Pair(1)) = 64 # bytes
     
"""


class Pair:
    __slots__ = ("first", "last")

    def __init__(self, first):
        self.first = first
        self.last = None

    def get_distance(self):
        if self.last is not None:
            return self.last - self.first
        return 0


def solution(source_data: list):
    meeting_pairs = get_pair_from_list(source_data)
    distance = get_max_distance_from_pairs(meeting_pairs)
    return distance


def get_pair_from_list(source_data: Iterable) -> Dict[int, Dict]:
    # first step - get pair (first meeting, last meeting)
    meeting_pairs = dict()
    for i, key in enumerate(source_data):
        if key not in meeting_pairs:
            meeting_pairs[key] = Pair(i)
        else:
            meeting_pairs[key].last = i
    return meeting_pairs


def get_max_distance_from_pairs(pairs:  Dict[int, Dict]) -> int:
    # second step - get the max difference
    result = 0
    for key in pairs:
        pair = pairs[key]
        result = max(result, pair.get_distance())
    return result


def get_data_list_from_file(file_path: str) -> Iterable:
    with open(file_path, "r") as file_with_data:
        for el in file_with_data:
            if el.strip().isnumeric():
                yield int(el)


if __name__ == "__main__":
    p = Pair(1)
    assert p.get_distance() == 0, p.get_distance()
    p = Pair(1)
    p.last = 10
    assert p.get_distance() == 9, p.get_distance()

    data_list = get_data_list_from_file("array.txt")
    start = time.time()
    res = solution(data_list)
    print(res)
    end = time.time()
    print(end - start)
    assert res == 9987, res
