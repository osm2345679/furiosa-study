from setting import get_llm
import time

llm = get_llm(max_tokens=2000)

prompts = [
    "NPU란?",
    "NPU와 GPU의 차이를 10가지 설명해줘",
    "NPU의 구조와 장점, 활용 분야를 꽤 자세히 설명해줘."
]

for prompt in prompts:
    start = time.perf_counter()
    response = llm.invoke(prompt)
    elapsed = time.perf_counter() - start

    print("질문 :", prompt)
    print("걸린 시간 :", round(elapsed, 2), "초")

# Results
# 질문 : NPU란?
# 걸린 시간 : 9.09 초
# 질문 : NPU와 GPU의 차이를 10가지 설명해줘
# 걸린 시간 : 14.26 초
# 질문 : NPU의 구조와 장점, 활용 분야를 꽤 자세히 설명해줘.
# 걸린 시간 : 15.96 초