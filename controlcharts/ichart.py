import numpy as np
import pandas as pd

def ichart(data,sigmas=3):
    if isinstance(data, pd.Series):
        nested_input = False
        series = list(data)
    else:
        try:
            series = data[data.keys()[0]]
            if len(data.keys()) != 1:
                raise ValueError('Nested iterable contains multiple data series')
            nested_input = True
        except AttributeError:
            series = data
            nested_input = False

    r = dict()
    stdev = np.std(series)
    mean = np.mean(series)
    lower_limit = mean - sigmas * stdev
    upper_limit = mean + sigmas * stdev

    make_series = lambda x: [x for _ in series]

    if nested_input:
        r = data
    else:
        r = { 'data': series }

    r['mean'] = make_series(mean)
    r['lower_limit'] = make_series(lower_limit)
    r['upper_limit'] = make_series(upper_limit)


    return r