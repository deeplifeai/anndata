import os


dataframe_provider = os.getenv('DATAFRAME_PROVIDER', default='pandas')

if dataframe_provider == 'pandas':
    from pandas import DataFrame as BaseDataFrame
elif dataframe_provider == 'vaex':
    from vaex.dataframe import DataFrame as BaseDataFrame


class DataFrame(BaseDataFrame):
    pass
