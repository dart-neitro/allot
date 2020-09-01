import time
"""

First: Run the following code using Python7+ (otherwise the type hints
will throw an error)

Second: Figure out what the function `solution` is doing

Third: Optimize the function `solution` to run under 2 seconds.
It is possible to run under a second.

"""

def solution(my_list: list):
    len_list = len(my_list)
    result = 0
    for i in range(len_list):
        for j in range(len_list):
            if my_list[i] == my_list[j]:
                result = max(result, abs(i - j))
    return result


if __name__ == "__main__":
    with open("array.txt", "r") as file:
        rand_array = file.read().split("\n")
        rand_array.pop()
        fixed_arr = list(map(int, rand_array))
    start = time.time()
    print(solution(fixed_arr))
    end = time.time()
    print(end - start)
