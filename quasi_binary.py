# problem: https://codeforces.com/group/kVkUp7ANGL/contest/324821/problem/B
from math import log10

# greedy taking nearlest binary number and reducing K by it, and repeating during K is greater than 0

# complexity:
# -time O(K*log10(K))
# -space O(K)


def nearlest_binary(k):
    if k < 10:
        return 1
    # greedy taking highest value which can be created
    # taking highest int
    power = int(log10(k))//1
    actual = 10**power
    position = power-1
    while position >= 0:
        if actual + 10**position <= k:
            actual = 10**position + actual
            position -= 1
        else:
            break

    return actual


def quasi_binary():
    k = int(input())
    q_binary = []

    while k > 0:
        new_binary = nearlest_binary(k)
        q_binary.append(new_binary)
        k -= new_binary
    print(len(q_binary))
    return " ".join(map(str,q_binary))


print(quasi_binary())