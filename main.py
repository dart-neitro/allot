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

"""


def solution(source_data: list):
    meeting_pairs = get_pair_from_list(source_data)
    distance = get_max_distance_from_pairs(meeting_pairs)
    return distance


def get_pair_from_list(source_data: Iterable) -> Dict[int, Dict]:
    # first step - get pair (first meeting, last meeting)
    meeting_pairs = dict()
    for i, key in enumerate(source_data):
        if key not in meeting_pairs:
            meeting_pairs[key] = {'first': i, 'last': None}
        else:
            meeting_pairs[key]['last'] = i
    return meeting_pairs


def get_max_distance_from_pairs(pairs:  Dict[int, Dict]) -> int:
    # second step - get the max difference
    result = 0
    for key in pairs:
        data = pairs[key]
        if data['last'] is not None:
            curr_dist = data['last'] - data['first']
            result = max(result, curr_dist)
    return result


def get_data_list_from_file(file_path: str) -> Iterable:
    with open(file_path, "r") as file_with_data:
        for el in file_with_data:
            if el.strip().isnumeric():
                yield int(el)


if __name__ == "__main__":
    data_list = get_data_list_from_file("array.txt")
    start = time.time()
    res = solution(data_list)
    print(res)
    end = time.time()
    print(end - start)
    assert res == 9987, res
