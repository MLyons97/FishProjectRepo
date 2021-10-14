import pandas as pd

import FishProject.config_manager as conf
import FishProject.App.PullingFromS3 as pulling

test_puller = pulling.Pulling_Class()

def test_pull_a_df():
    tested_csv = test_puller.pull_data_set(conf.BUCKETNAME, conf.TARTARE + '.csv')
    assert type(tested_csv) == pd.DataFrame
