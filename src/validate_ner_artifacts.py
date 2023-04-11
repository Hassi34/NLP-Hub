import argparse
from src.utils.common import read_yaml
from src.cloud_sync import CloudSync
from src.utils.app_logging import get_logger

from transformers import AutoModelForTokenClassification
from transformers import BertTokenizerFast
from transformers import pipeline

import sys

STAGE = "Validate NER Artifacts"

def validate_artifacts(config_path):
    logger.info("Started NER artifacts validation...")
    config = read_yaml(config_path)
    ner_model = config['artifacts']['NER_MODEL_DIR']
    model_fine_tuned = AutoModelForTokenClassification.from_pretrained(ner_model)
    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")
    nlp = pipeline("ner", model=model_fine_tuned, tokenizer=tokenizer)
    example = "My name is Hasnain and I live in Vietnam"
    ner_results = nlp(example)
    if isinstance(ner_results, list) and len(ner_results) == 3:
        logger.info("NER Artifacts validation has been passed")
    else:
        logger.info("Could not validate the NER Artifacts")
        cloud_sync.upload_logs()
        sys.exit(1)

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
        validate_artifacts(parsed_args.config)
        cloud_sync.upload_logs()
        logger.info(f'>>>>> stage "{STAGE}" completed!<<<<<\n')
    except Exception as e:
        cloud_sync.upload_logs()
        logger.exception(e)
        raise e