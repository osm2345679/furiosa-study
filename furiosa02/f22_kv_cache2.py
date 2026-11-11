from setting import run_once, get_cache_metrics

prompts = [
    "NPU란 무엇인가?",
    "NPU의 특징을 설명해줘." * 100,
    "NPU의 특징을 설명해줘." * 300,
]

for i, prompt in enumerate(prompts, 1): # index 1부터 시작
    # print(i)
    print(f"\n========== 실험 {i} ==========")

    result = run_once(prompt, 300)
    print("입력 토큰 :", result["input_tokens"])
    print("출력 토큰 :", result["output_tokens"])
    print("응답 시간 :", round(result["elapsed"], 2))

    print("\nKV Cache Metrics")
    get_cache_metrics()

# Results
# ========== 실험 1 ==========
# 입력 토큰 : 15
# 출력 토큰 : 300
# 응답 시간 : 2.46

# KV Cache Metrics

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 11621
# Prefix Cache 적중 횟수 : 5489
# Prefix Cache 적중률 : 47.23
# KV Cache 사용률 : 0.00

# ========== 실험 2 ==========
# 입력 토큰 : 909
# 출력 토큰 : 300
# 응답 시간 : 2.42

# KV Cache Metrics

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 12529
# Prefix Cache 적중 횟수 : 6397
# Prefix Cache 적중률 : 51.06
# KV Cache 사용률 : 0.00

# ========== 실험 3 ==========
# 입력 토큰 : 2709
# 출력 토큰 : 300
# 응답 시간 : 2.62

# KV Cache Metrics

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 15237
# Prefix Cache 적중 횟수 : 9105
# Prefix Cache 적중률 : 59.76
# KV Cache 사용률 : 0.00