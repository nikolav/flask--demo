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

# expose $PORT; [default=8000]
# ENV PORT 8000
EXPOSE 8000

# run start
CMD ["python", "/home/app/app.py"]
