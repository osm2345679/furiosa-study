#7-1 카피
"""
furfiosa-llm-serve furiosa-ai/Qwen3-8B-FP8
furiosa-llm serve furiosa-ai/gpt-oss-20b
furiosa-llm serve furiosa-ai/Llama-3.1-8B-Instruct <<< 안됨.
furiosa-llm serve furiosa-ai/Meta-Llama-3.1-8B-Instruct-FP8-dynamic
furfiosa-llm-serve furiosa-ai/Qwen3.5-0.5B <<< 안됨.
furfiosa-llm-serve furiosa-ai/Qwen3-4B-FP8

furiosa-llm serve furiosa-ai/Qwen3-4B-FP8 \
    --device npu:2 \
    --host 0.0.0.0 \
    --port 8000
"""

# from openai import OpenAI

# client = OpenAI(
#     base_url="http://127.0.0.1:8000/v1",
#     api_key="EMPTY"
# )

from langchain_openai import ChatOpenAI

max_tokens = 1000

llm = ChatOpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key="EMPTY",
    max_tokens=max_tokens,
    temperature=0, 
    top_p=0.9
)

# 모델 확인
# model = client.models.list().data[0].id

# 추론
# streaming = client.chat.completions.create(
#     model = model,
#     messages=[
#         {
#             "role" : "user",
#             "content" : "NPU와 GPU의 차이점을 설명해줘."
#         }
#     ],
#     max_tokens=1000,
#     stream=True
# )

# for chunk in streaming:
#     if chunk.choices:
#         content = chunk.choices[0].delta.content
#         if content:
#             print(content, end="", flush=True)

for chunk in llm.stream("NPU와 GPU의 차이점을 설명해줘."):
    print(chunk.content, end="", flush=True)