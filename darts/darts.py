def score(x, y):
    if x ** 2 + y ** 2 > 100:
        points = 0
    elif x ** 2 + y ** 2 > 25 and x ** 2 + y ** 2 <= 100:
        points = 1
    elif x ** 2 + y ** 2 > 1 and x ** 2 + y ** 2 <= 25:
        points = 5
    else:
        points = 10
    return points
