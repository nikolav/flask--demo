#!/bin/bash

docker compose up -d
docker exec -it app yarn
docker exec -it app yarn build
docker exec -it api python3 ./auto__db_setup.py



