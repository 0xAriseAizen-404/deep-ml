import numpy as np

def online_simple_regression(xs, ys):
    # return (N, 2) array of (w0, w1) after each point
    count_x, count_y = 0, 0
    mean_x, mean_y = 0, 0
    moment_xx, moment_xy = 0, 0
    n = 0

    res = []
    w0, w1 = 0, 0
    for x, y in zip(xs, ys):
        # mean_x = ((count_x - 1) * mean_x + x) / count_x
        # mean_y = ((count_y - 1) * mean_y + y) / count_y

        n += 1

        delta_x = x - mean_x
        mean_x = mean_x + delta_x / n
        
        delta_y = y - mean_y
        mean_y = mean_y + delta_y / n

        delta_x2 = x - mean_x
        delta_y2 = y - mean_y

        moment_xx = moment_xx + (delta_x * delta_x2)
        moment_xy = moment_xy + (delta_x * delta_y2)

        if moment_xx == 0:
            w1, w0 = 0.0, mean_y
        else:
            w1 = moment_xy / moment_xx
            w0 = mean_y - w1 * mean_x
        res.append([w0, w1])
        
    return np.array(res)