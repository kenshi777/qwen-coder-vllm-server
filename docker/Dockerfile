FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        build-essential \ 
        python3 \
        python3-pip \
        python3-dev && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/req.txt
RUN python3 -m pip install --no-cache-dir -r /tmp/req.txt && \
    python3 -m pip cache purge

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]