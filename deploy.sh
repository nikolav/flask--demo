#!/bin/bash


# run/build containers
docker compose up -d

# init database
docker exec -it api python3 ./auto__db_setup.py

# build ui
docker exec -it app yarn
docker exec -it app yarn build



