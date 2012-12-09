import numpy as np
import pandas as pd

def ichart(dataframe):
    if isinstance(dataframe, pd.DataFrame):
        if len(dataframe.columns) != 1:
            raise ValueError('`dataframe` may only contain one column.')
        column_name = dataframe.columns[0]
        series = dataframe[column_name]
    elif isinstance(dataframe, pd.Series):
        column_name = 'Data'
        series = dataframe

    stdev = np.std(series)
    mean = np.mean(series)
    lower_limit = mean - 3 * stdev
    upper_limit = mean + 3 * stdev

    make_series = lambda x: pd.Series([x for _ in series], index=dataframe.index)

    return pd.DataFrame({
        column_name: series
            , 'LCL': make_series(lower_limit)
            , 'UCL': make_series(upper_limit)
            , 'Mean': make_series(mean)
        })