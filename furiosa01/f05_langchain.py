#1 카피
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

# pip install langchain-openai
from langchain_openai import ChatOpenAI
                                                                
# client = OpenAI(
#     base_url="http://127.0.0.1:8000/v1",
#     api_key="EMPTY"
# )

# # 모델 확인
# models = client.models.list()
# model_id = models.data[0].id

llm = ChatOpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key="EMPTY"
)

# # 추론
# response = client.chat.completions.create(
#     model = model_id,
#     messages=[
#         {
#             "role" : "user",
#             "content" : "NPU와 GPU의 차이점을 설명해줘."
#         }
#     ],
#     max_tokens=1000
# )
response = llm.invoke("NPU와 GPU의 차이점을 설명해줘.")

# print(response.choices[0].message.content)
print(response.content)