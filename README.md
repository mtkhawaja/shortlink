# shortlink

[![tests](https://github.com/mtkhawaja/shortlink/actions/workflows/main.yml/badge.svg)](https://github.com/mtkhawaja/shortlink/actions/workflows/main.yml)
[![Docker Build](https://github.com/mtkhawaja/shortlink/actions/workflows/docker-image.yml/badge.svg)](https://github.com/mtkhawaja/shortlink/actions/workflows/docker-image.yml)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

- URL Shortener written in python.

## Quick Start

- Swagger [Documentation](https://shortlink-api.herokuapp.com/docs)

### Docker

#### Bash

```bash
docker build ./ -t shortlink/api -f ./Dockerfile && \
docker run -rm -it -p 80:8080 shortlink/api 
```

#### Powershell

```bash
docker build ./ -t shortlink/api -f ./Dockerfile; `
if ($?) {`
  docker run --rm -it -p 80:8080  shortlink/api; `
}
```

## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
