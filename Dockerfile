FROM python:3.7-slim
COPY install-chrome.sh install-chrome.sh
RUN sh install-chrome.sh
ENV DISPLAY=:99

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
