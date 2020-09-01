import time
from typing import List, Dict
"""

First: Run the following code using Python7+ (otherwise the type hints
will throw an error)

Second: Figure out what the function `solution` is doing

Third: Optimize the function `solution` to run under 2 seconds.
It is possible to run under a second.

"""


def solution(source_list: list):
    meeting_pairs = get_pair_from_list(source_list)
    distance = get_max_distance_from_pairs(meeting_pairs)
    return distance


def get_pair_from_list(source_list: List[int]) -> Dict[int, Dict]:
    # first step - get pair (first meeting, last meeting)
    meeting_pairs = dict()
    for i in range(len(source_list)):
        key = source_list[i]
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


if __name__ == "__main__":
    with open("array.txt", "r") as file:
        rand_array = file.read().split("\n")
        rand_array.pop()
        fixed_arr = list(map(int, rand_array))
    start = time.time()
    res = solution(fixed_arr)
    print(res)
    end = time.time()
    print(end - start)
    assert res == 9987, res
