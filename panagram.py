# problem: https://codeforces.com/problemset/problem/520/A

# complexity:
# -time O(K), where k is length of word
# -space O(1) -> 256


def panagram():
    letters = [False]*256
    # I don't need to use n value to declaration
    n = input()
    p = str(input())
    counter = 0
    # difference between lower and upper case in ASCI code is 32
    for letter in p:
        if letters[ord(letter)] is False:
            counter += 1
            # I made bigger array, from this reason I don't need to add if statement
            letters[ord(letter)] = True
            letters[ord(letter)-32] = True
            letters[ord(letter)+32] = True
    if counter == 26:
        return "YES"
    else:
        return "NO"


print(panagram())
