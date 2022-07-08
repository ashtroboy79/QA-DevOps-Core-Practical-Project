FROM python:3.8
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
RUN chmod +x gunicorn_starter.sh
EXPOSE 8000
ENTRYPOINT ["./gunicorn_starter.sh"]
