"""
furiosa-llm serve furiosa-ai/Qwen3-4B-FP8 \
    --device npu:2 \
    --host 127.0.0.1 \
    --port 8000
"""
from setting import get_llm

llm = get_llm(max_tokens=1000)

prompt = "NPU와 GPU의 차이를 설명해줘."

response = llm.invoke(prompt)

print(response.content)