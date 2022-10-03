FROM jjanzic/docker-python3-opencv

WORKDIR /app

COPY config.properties last_date_event.properties main.py ./

RUN pip install ConfigObj beautifulsoup4 requests python-telegram-bot

CMD ["/usr/local/bin/python", "main.py"]