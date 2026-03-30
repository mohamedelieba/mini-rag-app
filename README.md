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

```cp .env.example .env```

### run the FastAPI server

```uvicorn main:app --reload --host 0.0.0.0 --port 5000```