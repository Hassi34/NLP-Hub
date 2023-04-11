
from src.utils.common import read_yaml
from src.utils.s3_bucket import SimpleStorageService

config = read_yaml("configs/config.yaml")

BUCKET_NAME = config['s3_config']['BUCKET_NAME']
REGION = config['s3_config']['REGION']
S3_BLESSED_MODEL_FILE_PATH = config['s3_config']['BLESSED_MODEL_FILE_PATH']
S3_BLESSED_MODEL_CONFIG_FILE_PATH = config['s3_config']['BLESSED_MODEL_CONFIG_FILE_PATH']
S3_LOGS_FILE_PATH = config['s3_config']['LOGS_FILE_PATH']

BLESSED_MODEL_FILE_PATH = config['artifacts']['BLESSED_MODEL_FILE_PATH']
BLESSED_MODEL_CONFIG_FILE_PATH = config['artifacts']['BLESSED_MODEL_CONFIG_FILE_PATH']
LOGS_FILE_PATH = config['logs']['RUNNING_LOGS_FILE_PATH']

class CloudSync:
    def __init__(self):
        self.s3 = SimpleStorageService(region_name= REGION,
                                s3_bucket_name= BUCKET_NAME)

    def upload_ner_config(self):
        self.s3.upload_file(BLESSED_MODEL_CONFIG_FILE_PATH,
                             S3_BLESSED_MODEL_CONFIG_FILE_PATH)
        
    def upload_ner_pytorch_model(self):
        self.s3.upload_file(BLESSED_MODEL_FILE_PATH,
                             S3_BLESSED_MODEL_FILE_PATH)

    def download_ner_config(self):
         self.s3.download_file(BLESSED_MODEL_CONFIG_FILE_PATH,
                             S3_BLESSED_MODEL_CONFIG_FILE_PATH)

    def download_ner_pytorch_model(self):
         self.s3.download_file(BLESSED_MODEL_FILE_PATH,
                             S3_BLESSED_MODEL_FILE_PATH)
         
    def upload_logs(self):
        self.s3.upload_file(LOGS_FILE_PATH,
                            S3_LOGS_FILE_PATH)
