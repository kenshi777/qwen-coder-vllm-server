#!/usr/bin/env bash
set -e

exec vllm serve kenshi777/qwen-1.7b-coder-4bit \
    --quantization bitsandbytes \
    --dtype auto \
    --gpu-memory-utilization 0.8 \
    --max-model-len 512 \
    --host 0.0.0.0 \
    --port 8000