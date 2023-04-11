
#!/bin/bash -eo pipefail
echo [$(date)]: ">>>>>>>>>>>>>>>>>> TRAINING ENVIRONMENT SETUP >>>>>>>>>>>>>>>>>>"
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Install Miniconda >>>>>>>>>>>>>>>>>>"
apt update
apt install wget
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
export PATH="/root/miniconda3/bin:${PATH}"
echo "Running $(conda --version)"
conda init bash
. /root/.bashrc
conda update -n base -c defaults conda -y
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Create Environment >>>>>>>>>>>>>>>>>>"
conda create -n myenv python=3.10 -y
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Activate Environment >>>>>>>>>>>>>>>>>>"
conda activate myenv
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Install Requirements >>>>>>>>>>>>>>>>>>"
pip install -r requirements.txt
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Project Folder Structure >>>>>>>>>>>>>>>>>>"
python template.py
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Download data from Source >>>>>>>>>>>>>>>>>>"
python src/download_artifacts.py --config=configs/config.yaml
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Model Validation >>>>>>>>>>>>>>>>>>"
python src/validate_ner_artifacts.py --config=configs/config.yaml
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Copy NER blessed model to serving >>>>>>>>>>>>>>>>>>"
cp -r artifacts/ner_model model_serving/src/production_models/
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Copy Config to serving >>>>>>>>>>>>>>>>>>"
cp configs/config.yaml model_serving/src/configs/config.yaml
echo [$(date)]: ">>>>>>>>>>>>>>>>>> Copy Common Utils to serving >>>>>>>>>>>>>>>>>>"
cp src/utils/common.py model_serving/src/utils/common.py
echo [$(date)]: ">>>>>>>>>>>>>>>>>> TRAINING COMPLETED >>>>>>>>>>>>>>>>>>"