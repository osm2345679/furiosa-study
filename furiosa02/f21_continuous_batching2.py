from concurrent.futures import ThreadPoolExecutor
from setting import run_once
import statistics
import time

prompts = [
    f"NPU 추론 최적화방법 {i}번을 자세히 설명해줘." for i in range(8)
]

# print(prompts)  # ['NPU 추론 최적화방법 0번을 자세히 설명해줘.', ... 'NPU 추론 최적화방법 7번을 자세히 설명해줘.']
# print(len(prompts)) # 8

# results = run_once("NPU가 뭐게?", 1000)
# print(results["text"])

def ask(prompt):
    return run_once(prompt, 100)

for workers in [1, 2, 4, 8]:
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(
            pool.map(
                lambda prompts:run_once(prompts, 50),  # lambda는 익명 함수 한 줄로 작성할 수 있게 해줌.
                prompts
            )
        )
    elapsed = time.perf_counter() - start

    total_tokens = sum(
        r['output_tokens'] for r in results  # results가 thread마다 있으므로 반복문으로 output_token 추출
    )

    avg_latency = statistics.mean(
        r["elapsed"] for r in results
    )

    print(f"\n동시 요청 수: {workers}")
    print(f"전체 시간: {elapsed:.2f}초")
    print(f"전체 출력 토큰: {total_tokens}")
    print(f"처리량: {total_tokens / elapsed:.2f} TPS")
    print(f"평균 요청 지연: {avg_latency:.2f}초")

# Results
# 동시 요청 수: 1
# 전체 시간: 6.71초
# 전체 출력 토큰: 800
# 처리량: 119.19 TPS
# 평균 요청 지연: 0.80초

# 동시 요청 수: 2
# 전체 시간: 3.60초
# 전체 출력 토큰: 800
# 처리량: 222.20 TPS
# 평균 요청 지연: 0.90초

# 동시 요청 수: 4
# 전체 시간: 1.92초
# 전체 출력 토큰: 800
# 처리량: 416.36 TPS
# 평균 요청 지연: 0.96초

# 동시 요청 수: 8
# 전체 시간: 1.03초
# 전체 출력 토큰: 800
# 처리량: 777.52 TPS
# 평균 요청 지연: 1.02초