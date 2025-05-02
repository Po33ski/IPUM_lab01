#I changed here a few things but the most important is for me this one: RUN pip install --no-cache-dir .
#After that I could execute docker build -t ml-app . successful 
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

# Install dependencies directly using pip
RUN pip install --no-cache-dir .

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]












