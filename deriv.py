def deriv(f_left, f_c, f_right, type_left, type_c, type_right, h):
    if type_left == 0 and type_c == 0 and type_right == 0:
        v = 0

    elif type_left == 0:
        v = (f_right - f_c) / h

    elif type_right == 0:
        v = (f_c - f_left) / h

    elif type_c == 0 and type_right != 0 and type_left != 0:
        v = (f_c - f_left) / h

    else:
        v = (f_right - f_left) / (2 * h)

    return v
