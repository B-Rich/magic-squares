def rotate90(matrix):
    return [[row[-1-i] for row in matrix] for i in range(len(matrix[0]))]

def equ(matrix,i):
    return [[eq1(item,i) for item in row] for row in matrix]

def eq1(a,b):
    if a==b:
        return 1
    return 0

def char(i):
    if i==0:
        return " "
    if i==1:
        return u"\u2588"
    if i==2:
        return u"\u259B"
    if i==3:
        return u"\u259F"
    if i==4:
        return u"\u259C"
    if i==5:
        return u"\u2599"

def ascii_char(i):
    if i==1:
        return "#"
    else:
        return " "

def to_int(current):
    return int("".join(["".join([str(i) for i in row]) for row in current]))

def replace(ls, p):
    return [[p[i-1] for i in row] for row in ls]

def permute(ls, p):
    return [ls[p[0]],ls[p[1]],ls[p[2]]]

def sum_three(thing):
    tot = 0
    for a in thing:
        for b in a.matrix:
            tot += sum(b)
    return tot
