# RPS : Request Per Second
# 26 카피
from concurrent.futures import ThreadPoolExecutor
from setting import get_llm
import time

llm = get_llm(max_tokens=1000)

prompts = [
    f"NPU 추론 최적화 방법 {i}번을 설명해줘" for i in range(8)
]

def ask(prompt):
    response = llm.invoke(prompt)
    usage = response.usage_metadata or {}
    return usage.get("output_tokens", 0)

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as executor:
    tokens = list(executor.map(ask, prompts))

elapsed = time.perf_counter() - start

total_tokens = sum(tokens)

print("전체 출력 토큰 :", total_tokens)
print("전체 시간 :", round(elapsed, 2), "초")
print("Ouput TPS :", round(total_tokens / elapsed, 2))
print("RPS :", round(len(prompts) / elapsed, 2))

# Results
# 전체 출력 토큰 : 8000
# 전체 시간 : 18.81 초
# Ouput TPS : 425.21
# RPS : 0.43