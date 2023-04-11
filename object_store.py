from s3 import SimpleStorageService

class CloudSync:
    def __init__(self):
        self.s3 = SimpleStorageService(region_name= "us-east-2",
                                s3_bucket_name= "nlp-hub")

    def upload_ner_config(self):
        self.s3.upload_file("artifacts/ner_model/config.json",
                             "ner_model/config.json")
        
    def upload_ner_pytorch_model(self):
        self.s3.upload_file("artifacts/ner_model/pytorch_model.bin",
                             "ner_model/pytorch_model.bin")

    def download_ner_pytorch_model(self):
         self.s3.download_file("artifacts/ner_model/pytorch_model.bin",
                             "ner_model/pytorch_model.bin")

    def download_ner_config(self):
         self.s3.download_file("artifacts/ner_model/config.json",
                             "ner_model/config.json")

sync = CloudSync()
#sync.upload_ner_pytorch_model()
#sync.download_ner_config()
#sync.download_ner_pytorch_model()