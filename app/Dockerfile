# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

# install node, yarn; build
# RUN curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -; apt-get install -y nodejs; curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -; echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list; apt update; apt install yarn;
RUN apk add --update nodejs npm; npm install --global yarn
RUN yarn; yarn build

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM builder as dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
