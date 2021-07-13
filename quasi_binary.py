# problem: https://codeforces.com/group/kVkUp7ANGL/contest/324821/problem/B
from math import log10


# complexity:
# -time O(K*log10(K))
# -space O(K)


def nearlest_binary(k):
    if k < 10:
        return 1
    power = int(log10(k))//1
    actual = 0
    position = power
    while position >= 0:
        # if on actual 10^power %10 != 0, than taking this value
        if k//10**position:
            actual += 10**position
            k%=10**position
        position -= 1
        
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