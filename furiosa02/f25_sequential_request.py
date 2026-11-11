# 24 카피

from setting import get_llm
import time

llm = get_llm(max_tokens=1000)

prompts = [
    f"NPU 추론 최적화 방법 {i}번을 설명해줘" for i in range(8)
]

start = time.perf_counter()
for prompt in prompts:
    llm.invoke(prompt)
elapsed = time.perf_counter() - start

print("전체 요청 :", len(prompts))
print("전체 소요 시간 :", round(elapsed,  3), "초")
print("요청 처리량 :", round(len(prompts) / elapsed, 3), "req/s")

# Results
# 전체 요청 : 8
# 전체 소요 시간 : 64.206 초
# 요청 처리량 : 0.125 req/s