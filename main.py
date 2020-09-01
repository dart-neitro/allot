import time
"""

First: Run the following code using Python7+ (otherwise the type hints
will throw an error)

Second: Figure out what the function `solution` is doing

Third: Optimize the function `solution` to run under 2 seconds.
It is possible to run under a second.

"""


def solution_old(my_list: list):
    len_list = len(my_list)
    result = 0
    for i in range(len_list):
        for j in range(len_list):
            if my_list[i] == my_list[j]:
                result = max(result, abs(i - j))
    return result


def solution(my_list: list):
    len_list = len(my_list)

    # first step - get pair (first meeting, last meeting)
    meeting_pairs = dict()
    for i in range(len_list):
        key = my_list[i]
        if key not in meeting_pairs:
            meeting_pairs[key] = {'first': i, 'last': None}
        else:
            meeting_pairs[key]['last'] = i

    # second step - get the max difference
    result = 0
    for key in meeting_pairs:
        data = meeting_pairs[key]
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
