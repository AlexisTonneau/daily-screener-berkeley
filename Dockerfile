FROM python:3.7-slim
COPY install-chrome.sh install-chrome.sh
RUN sh install-chrome.sh
ENV DISPLAY=:99

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


CMD ["python", "app.py"]
