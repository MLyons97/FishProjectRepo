import pandas
import boto3
import pprint

import FishProject.config_manager as conf

class Pulling_Class():
    def __init__(self):
        self.__s3_client = boto3.client('s3')

    @property
    def get_client(self):
        return self.__s3_client

    def pull_data_set(self, bucket_name: str, key: str):
        bucket_contents = self.get_client.get_object(Bucket=bucket_name, Key=key)
        csv_body = pandas.read_csv(bucket_contents["Body"])
        return csv_body


test_class = Pulling_Class()

bucket_name = conf.BUCKETNAME
test_prefix = conf.TARTARE + '.csv'
test_csv = test_class.pull_data_set(bucket_name, test_prefix)
pprint.pprint(test_csv)