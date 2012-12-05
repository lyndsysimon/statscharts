import numpy as np
import pandas as pd

def ichart_limits(dataset):
    if len(dataset.columns) != 1:
        raise ValueError('`Dataset` must be a pandas Dataset with one column.')

    series = dataset[dataset.columns[0]]
    stdev = np.std(series)
    mean = np.mean(series)
    lower_limit = mean - 3 * stdev
    upper_limit = mean + 3 * stdev

    make_series = lambda x: pd.Series([x for _ in series])

    return pd.DataFrame({
        dataset.columns[0]: series
            , 'LCL': make_series(lower_limit)
            , 'UCL': make_series(upper_limit)
            , 'Mean': make_series(mean)
        })






if __name__ == '__main__':
    DATASET = [3.9756983644,3.7713126251,3.3275001762,3.6391279767,3.0765596079,3.9051652765,3.0581050608,3.0522579723,3.6764779016,3.3856052374,3.6913859495,3.7530375095,3.2907705139,3.7494910103,3.8052954823,3.9672484156,3.1350962478,3.4966814318,3.7202859251]

    LCL = 2.60747305894136
    MEAN = 3.55142645709413
    UCL = 4.4953798552469
    STDEV = 0.31465113271759

    d = pd.DataFrame(pd.Series(DATASET), columns=['primary',])

    chart = ichart_limits(d)

    print chart