from setting import get_llm
import time

llm = get_llm(max_tokens=1000)

start = time.perf_counter()
response = llm.invoke("NPU의 장점을 세 가지 설명해줘.")
elapsed = time.perf_counter() - start

usage = response.usage_metadata or {}

print("응답 :", response.content)
print("지연시간 :", round(elapsed, 3), "초")
print("입력 토큰 :", usage.get("input_tokens", 0))
print("출력 토큰 :", usage.get("output_tokens", 0))

# Results
# 응답 : <think>
# ...
# 이러한 특성 덕분에 NPU는 AI 기반의 스마트 기기, 자율주행, 의료 기술 등 다양한 분야에서 활용되고 있습니다.
# 지연시간 : 5.337 초
# 입력 토큰 : 19
# 출력 토큰 : 657
