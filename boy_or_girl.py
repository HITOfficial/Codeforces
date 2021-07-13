# problem: https://codeforces.com/problemset/problem/236/A

# checking if number of distinct letters is odd or even

# complexity:
# -time O(K)
# -space O(1) -> 256


def boy_or_girl():
    p = input()
    letters = [False]*256
    counter = 0
    for letter in p:
        if letters[ord(letter)] == False:
            letters[ord(letter)] = True
            counter += 1
    if counter%2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


print(boy_or_girl())