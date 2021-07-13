# problem: https://codeforces.com/group/kVkUp7ANGL/contest/324821/problem/C
# idea from: https://www.programmersought.com/article/35134638693/

# dynamic memorizing length of ascending column

# complexity:
# -time O(k*m)
# -space O(n*m)


def find_column(answers,l,r,m):
    if l == r:
        return True
    for i in range(m):
        if answers[r][i] - answers[l][i] == r-l:
            return True
    return False


def help_Alyona():
    size = [int(el) for el in input().split()]
    n, m = size[0], size[1]
    array = [[int(el) for el in input().split()] for _ in range(n)]
    k = int(input())
    questions = [[int(el)-1 for el in input().split()] for _ in range(k)]

    # f(i,j) = f(i-1,j)+1  <=> array[i][j] >= array[i-1][j], else f(i,j) = f(i-1,j) and than starting row doesn't need to be checked
    answers = [[0]*m for _ in range(n)]
    answers[0] = [1]*m
    for i in range(1,n):
        for j in range(m):
            if array[i][j] >= array[i-1][j]:
                answers[i][j] = answers[i-1][j]+1
            else:
                answers[i][j] = answers[i-1][j]

    answer = ""
    for l,r in questions:
        if find_column(answers,l,r,m):
            answer +="\nYes"
        else:
            answer +="\nNo"

    return answer


print(help_Alyona())