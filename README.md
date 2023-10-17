## flask.app@docker

@host
   IS_PRODUCTION = True // @api/src/config/vars.py
   IS_PRODUCTION = True // @app/src/config/vars.ts

```
$ docker compose up -d
[+] Building 1.1s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                                       0.0s
    ...                                                                                                                                         0.0s
 => => naming to docker.io/library/flask_web                                                                                                                                                                                               0.0s
[+] Running 2/2
 ⠿ Network flask_default  Created                                                                                                                                                                                                          0.0s
 ⠿ Container flask-web-1  Started

$ docker compose ps
NAME                COMMAND             SERVICE             STATUS              PORTS
flask-web-1         "python3 app.py"    web                 running             0.0.0.0:8000->8000/tcp

$ curl localhost:8000
Hello World!

$ docker compose down
```
