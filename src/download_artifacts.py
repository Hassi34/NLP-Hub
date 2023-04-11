import argparse
from src.utils.common import read_yaml
from src.cloud_sync import CloudSync
from src.utils.app_logging import get_logger

STAGE = "Download Artifacts"

def download_artifacts():

    logger.info("Downloading NER artifacts from the s3 source...")
    cloud_sync.download_ner_config()
    cloud_sync.download_ner_pytorch_model()
    logger.info("Artifacts have been saved locally")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()
    cloud_sync = CloudSync()
    config = read_yaml(parsed_args.config)
    LOGS_FILE_PATH = config['logs']['RUNNING_LOGS_FILE_PATH']
    logger = get_logger(LOGS_FILE_PATH)
    try:
        logger.info("\n********************")
        logger.info(f'>>>>> stage "{STAGE}" started <<<<<')
        download_artifacts()
        #cloud_sync.upload_logs()
        logger.info(f'>>>>> stage "{STAGE}" completed!<<<<<\n')
    except Exception as e:
        cloud_sync.upload_logs()
        logger.exception(e)
        raise e