import FishProject.App.PullingFromS3 as pulling
import FishProject.App.DF_Manipulator as manip

import pprint as pp

pulling_class = pulling.Pulling_Class()
data_frame_manipulator = manip.DataManipulator()
bucket_name = pulling_class.get_bucket_name

fish_df1 = pulling_class.pull_data_set(bucket_name, pulling_class.get_fish_string_list[0])
fish_df_mon = pulling_class.pull_data_set(bucket_name, pulling_class.get_fish_string_list[1])
fish_df_tues = pulling_class.pull_data_set(bucket_name, pulling_class.get_fish_string_list[2])

full_fish_df = data_frame_manipulator.appender(fish_df1, fish_df_mon, fish_df_tues)

pp.pprint(full_fish_df)