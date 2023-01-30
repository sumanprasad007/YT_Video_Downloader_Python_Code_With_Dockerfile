FROM python:3.8-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python","yt_video_downloader.py" ]