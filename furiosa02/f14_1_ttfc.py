# Time to First Chunk
from setting import get_llm
import time

llm = get_llm(max_tokens=500)

prompt = "NPU의 장점을 자세히 설명해줘."

start = time.perf_counter()
first_time = None

for chunk in llm.stream(prompt):
    if chunk.content:
        if first_time is None:
            first_time = time.perf_counter()
        print(chunk.content, end="",flush=True)

print("========================================")
print("첫 컨텐츠 응답 시간 :", round(first_time-start, 2), "초")

# Results
# ========================================
# 첫 컨텐츠 응답 시간 : 0.03 초