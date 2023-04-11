FROM python:3.10-slim

LABEL maintainer="hasanain@aicaliber.com"

EXPOSE 443 80 8080

WORKDIR /model_serving

COPY ./model_serving/ .

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "src/main.py"]