from setting import get_llm

llm = get_llm(max_tokens=500)

response = llm.invoke("NPU란 무엇인가")

print(response.content)
print(response.usage_metadata)

# Results
# NPU는 **Neural Processing Unit**의 약자로,
# ...
# NPU는 AI 기술의 발전과 함께, 다양한 산업(의료, 교통, 제조 등)에서 혁신적인 솔루션을 제공하고 있습니다.
# {'input_tokens': 14, 'output_tokens': 1236, 'total_tokens': 1250,
# 'input_token_details': {'audio': 0, 'cache_read': 6}, 'output_token_details': {'audio': 0, 'reasoning': 0}}