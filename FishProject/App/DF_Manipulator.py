import FishProject.App.PullingFromS3 as pulling

import pandas as pd

class DataManipulator:
    def __init__(self):
        pass

    @staticmethod
    def appender(*args: pd.DataFrame):
        df_list = [x for x in args]
        returning_df = pd.concat(df_list)
        return returning_df

    def avg_finder(self, dataframe: pd.DataFrame):
        pass


test_manipulator = DataManipulator()
