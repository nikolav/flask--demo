#!/bin/bash

docker compose up -d
docker exec -it app yarn
docker exec -it app yarn build
# docker exec -it api python3 commands:run_db_setup.py
