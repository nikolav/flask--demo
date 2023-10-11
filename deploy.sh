#!/bin/bash


# run containers
docker compose up -d

# build ui
docker exec -it app yarn
docker exec -it app yarn build

# init database
docker exec -it api python3 auto__db_setup.py


