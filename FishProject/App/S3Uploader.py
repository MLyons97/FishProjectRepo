import json


class S3Uploader:

    def __init__(self):
        pass

    @staticmethod
    def upload_file(file: dict, filename: str, bucket_name: str, full_key: str, s3_client, file_type="json"):
        if file_type == "json":
            full_filename = filename + "." + file_type
            with open(full_filename, 'w') as json_file:
                json.dump(file, json_file)
            s3_client.upload_file(Filename=full_filename,
                                  Bucket=bucket_name,
                                  Key=full_key)
        else:
            print("Would be great fun if this bit was coded...")