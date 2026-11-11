# Time to First Chunk
from setting import get_llm
import time

llm = get_llm(max_tokens=500)

prompt = "NPU의 장점을 자세히 설명해줘."

start = time.perf_counter()

chunk = next(iter(llm.stream(prompt)))

first_time = time.perf_counter() - start

print("========================================")
print("첫 컨텐츠 응답 시간 :", round(first_time, 2), "초")

# Results
# ========================================
# 첫 컨텐츠 응답 시간 : 0.03 초