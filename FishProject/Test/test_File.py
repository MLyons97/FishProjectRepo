import pandas as pd

import FishProject.config_manager as conf
import FishProject.App.PullingFromS3 as pulling
import FishProject.App.DF_Manipulator as manip

test_puller = pulling.Pulling_Class()

def test_pull_a_df():
    tested_csv = test_puller.pull_data_set(conf.BUCKETNAME, conf.TARTARE + '.csv')
    assert type(tested_csv) == pd.DataFrame

test_manipulator = manip.DataManipulator()

def test_summing_two_dfs():
    test_data1 = [['a', 1], ['b', 2], ['c', 3]]
    test_df1 = pd.DataFrame(test_data1)
    test_df2 = pd.DataFrame([['a', 4], ['b', 5], ['c', 6]])
    new_df = test_manipulator.appender(test_df1, test_df2)
    reference_df = pd.DataFrame([['a', 1], ['b', 2], ['c', 3], ['a', 4], ['b', 5], ['c', 6]],
                                index=[0, 1, 2, 0, 1, 2])
    print(reference_df)
    pd.testing.assert_frame_equal(new_df, reference_df)
