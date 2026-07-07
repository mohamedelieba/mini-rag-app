# mini-rag-app

## Requirements

- python 3.12 or later

### Install python using Miniconda

1) Download and install MiniConda from [here](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
2) Create new environment ```conda create -n mini-rag-app```
3) Activate the environment ```conda activate mini-rag-app```

## Installation

```pip install -r requirements.txt```

### setup your environment variable

```bash 
$ cp .env.example .env
```
### Run docker compose to start mongodb

```bash
$ cd docker
$ cp .env.example .env

- update `.env` with your mongodb credentials

$ docker compse up
```
### run the FastAPI server

```uvicorn main:app --reload --host 0.0.0.0 --port 5000```