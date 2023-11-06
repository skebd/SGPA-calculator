def subject():
    a = int(input('21MAT41: '))
    b = int(input('21CS42: '))
    c = int(input('21CS43: '))
    d = int(input('21CS44: '))
    e = int(input('21BE45: '))
    f = int(input('21CSL46: '))
    g = int(input('21CSL481: '))
    h = int(input('21CIP47: '))
    i = int(input('21UH49: '))
    j = int(input('21INT49: '))

    sub1 = 3 * grade(a)
    sub2 = 4 * grade(b)
    sub3 = 4 * grade(c)
    sub4 = 3 * grade(d)
    sub5 = 2 * grade(e)
    sub6 = 1 * grade(f)
    sub7 = 1 * grade(g)
    sub8 = 1 * grade(h)
    sub9 = 1 * grade(i)
    sub10 = 2 * grade(j)
    res = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9 + sub10) / 22
    print(res)


def grade(y):
    if y < 40:
        return 0
    elif 40 <= y < 45:
        return 4
    elif 45 <= y < 50:
        return 5
    elif 50 <= y < 60:
        return 6
    elif 60 <= y < 70:
        return 7
    elif 70 <= y < 80:
        return 8
    elif 80 <= y < 90:
        return 9
    elif 90 <= y < 100:
        return 10


subject()
