# problem: https://codeforces.com/contest/903/problem/D
# idea: https://www.programmersought.com/article/86646430026/


# complexity:
# -time O(N)
# space O(1) -> 10**9

import numpy as np


#  solution using static array from numpy

def almost_difference_numpy():
    n = int(input())
    if n == 1:
        return 0

    # int from 1... -> 10^9
    # normal array declaration took over 3s. so used array from numpy
    count_equal = np.zeros(10**9+1)
    array = [int(el) for el in input().split()]
    ad_sum = 0
    prev_sum = 0
    for i in range(n):
        # formula from the: https://www.programmersought.com/article/86646430026/
        ad_sum = ad_sum + i * array[i] - prev_sum +count_equal[array[i]+1] - count_equal[array[i]-1]
        count_equal[array[i]] += 1
        prev_sum += array[i]
 
    return ad_sum
 
 
# becouse numpy doesn't work on codeforces I used set to memorize number of numbers

def almost_difference_dict():
    n = int(input())
    if n == 1:
        return 0
    dict_equal = dict()
    array = [int(el) for el in input().split()]
    ad_sum = 0
    prev_sum = 0

    for i in range(n):
        if not array[i] in dict_equal.keys():
            dict_equal[array[i]] = 0
        if not array[i]-1 in dict_equal.keys():
            dict_equal[array[i]-1] = 0
        if not array[i]+1 in dict_equal.keys():
            dict_equal[array[i]+1] = 0

        # formula from the: https://www.programmersought.com/article/86646430026/
        ad_sum = ad_sum + i * array[i] - prev_sum +dict_equal[array[i]+1] - dict_equal[array[i]-1]
        dict_equal[array[i]] += 1
        prev_sum += array[i]
 
    return ad_sum


# numpy
print(almost_difference_numpy())

# dictionary
print(almost_difference_dict())
