def force(p, x, y):
    fx = 0
    fy = 0
    h = 0.01

    for i in range(0, len(x) - 1):
        if x[i] < x[i + 1]:
            fx = fx + h * (p[i] + p[i + 1]) / 2

        elif x[i + 1] < x[i]:
            fx = fx + (-h) * (p[i] + p[i + 1]) / 2

        if y[i] < y[i + 1]:
            fy = fy + (-h) * (p[i] + p[i + 1]) / 2

        elif y[i + 1] < y[i]:
            fy = fy + h * (p[i] + p[i + 1]) / 2

    return fx, fy
