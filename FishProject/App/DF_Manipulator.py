import pandas as pd


class DataManipulator:
    def __init__(self):
        pass

    @staticmethod
    def appender(*args: pd.DataFrame):
        df_list = [x for x in args]
        returning_df = pd.concat(df_list)
        return returning_df

    @staticmethod
    def df_to_dict(dataframe: pd.DataFrame):
        return dataframe.to_dict()

    def avg_finder(self, dataframe: pd.DataFrame):
        return dataframe.groupby('Species').mean()
