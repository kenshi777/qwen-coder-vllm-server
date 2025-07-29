# Qwen‑1.7B‑Coder-4bit vLLM Server

Serve the **XformAI‑india/qwen‑1.7b‑coder** model quantised to 4‑bit with
[bitsandbytes](https://github.com/TimDettmers/bitsandbytes) through the blazing‑fast
[vLLM](https://github.com/vllm-project/vllm) engine. The container exposes an
OpenAI‑compatible REST endpoint, so existing tooling (LangChain, OpenAI SDK, curl)
“just works”.

## Features

* **4‑bit quantisation (bnb‑4bit)** — <3 GB VRAM footprint for 1.7 B params.
* **vLLM PagedAttention** — high throughput + long context with minimal GPU memory.
* **Drop‑in OpenAI API** — `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`.
* **Single‑command Docker run** — no local Python mess.
* **GitHub Actions CI/CD** — automatic multi‑arch image builds & pushes to GHCR.
* **Compose / K8s ready** — sample `docker‑compose.yml`.

## Quick Start

### 1. Clone + quantise (run once)
```bash
git clone https://github.com/kenshi777/qwen-coder-vllm-server.git
cd qwen-coder-vllm-server

python quantize.py
```
The script pushes a repo `kenshi777/qwen‑1.7b‑coder‑4bit` to the Hub.

### 2. Build & run

```bash
docker compose up --build
curl -X POST http://localhost:8000/v1/chat/completions \
     -H "Content-Type: application/json" \
     --data @example/request.json
```