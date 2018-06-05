import pandas as pd

def slice(data_frame, column_name, lower_limit=None, upper_limit=None, including_limits=False):
    returned_df = None

    if lower_limit is None and upper_limit is None:
        return data_frame

    if lower_limit is None:
        lower_limit = data_frame[column_name].min()
        return slice_below(data_frame, column_name, upper_limit, including_limits)

    if upper_limit is None:
        upper_limit = data_frame[column_name].max()
        return slice_above(data_frame, column_name, lower_limit, including_limits)

    returned_df = slice_above(data_frame, column_name, lower_limit, including_limits)
    returned_df = slice_below(returned_df, column_name, upper_limit, including_limits)

    return returned_df

def slice_above(data_frame, column_name, limit, including_limit=False):
    filter = None

    if including_limit:
        filter = data_frame[column_name] >= limit
    else:
        filter = data_frame[column_name] > limit

    return data_frame[filter]

def slice_below(data_frame, column_name, limit, including_limit=False):
    filter = None

    if including_limit:
        filter = data_frame[column_name] <= limit
    else:
        filter = data_frame[column_name] < limit

    return data_frame[filter]
