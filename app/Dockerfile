FROM python:3
RUN apt update; apt-get update

# mount-path in contanier
WORKDIR /home/app

# install flask
RUN pip install flask

# copy app
COPY . .

# bind volume
VOLUME .:/home/app

# expose $PORT; [default=5000]
ENV PORT 5000
EXPOSE $PORT

# run start
CMD ["python", "app.py"]
