# problem: https://codeforces.com/problemset/problem/479/B

from bisect import bisect_left


# complexity:
# -time O(KlogN) -> N(logK)^2 / NlogN <- sorting array
# -space O(N)


# somethink is wrong with tests second test on codeforces in template is good and answeris  with lower m, than on the submition tester


def towers():
    space = [int(el) for el in input().split()]
    n, k = space[0], space[1]
    array = [int(el) for el in input().split()]

    array = [(el, index) for el, index in zip(array, range(n))]
    array.sort()
    # separated indexes and values to do not modyfiy bisect
    array, array_ids = [value for value, _ in array], [
        index for _, index in array]

    moves = []
    m = 0
    s = 0

    # greedy reducing number of highest number by one and incrementing it to lowest, and checking if it changes instability
    while m < k:
        lowest, lowest_id = array.pop(0), array_ids.pop(0)
        highest, highest_id = array.pop(), array_ids.pop()
        if abs(highest-lowest) == 1 and n % 2 == 1:
            break
        # instability before changing cube
        s = highest-lowest
        # reducing values
        lowest, highest = lowest+1, highest-1
        # lowest
        new_lowest_id = bisect_left(array, lowest)
        array.insert(new_lowest_id, lowest)
        array_ids.insert(new_lowest_id, lowest_id)
        # highest
        new_highest_id = bisect_left(array, highest)
        array.insert(new_highest_id, highest)
        array_ids.insert(new_highest_id, highest_id)
        # instability
        tmp_s = highest-lowest
        # now is a best option
        if tmp_s >= s:
            break
        else:
            s = tmp_s
            moves.append((highest_id+1, lowest_id+1))
            m += 1

    mvs = ""
    for a, b in moves:
        mvs += str(a) + " " + str(b) + "\n"
    answer = "" + str(s) + " " + str(m)+"\n" + mvs
    return answer


print(towers())
