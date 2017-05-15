import numpy as np

def reject_outliers(data):
    data1 = data.astype(np.float)
    m = 2
    u = np.median(data1)
    s = np.std(data1)
    filtered = [e for e in data1 if (u - 2 * s < e < u + 2 * s)]
    return filtered
