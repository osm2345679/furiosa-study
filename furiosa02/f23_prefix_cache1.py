from setting import run_once, get_cache_metrics

prefix = "NPU 추론 최적화이 대한 설명입니다." * 150

for i in range(1, 5):
    prompt = prefix + f"\n질문 {i}: KV Cache란?"

    print(f"\n===== {i}회 요청 =====")
    result = run_once(prompt, 100)

    print("응답 시간 :", round(result["elapsed"], 3))
    print("입력 토큰 :", result["input_tokens"])

    print("\nPrefix Cache Metrics")
    get_cache_metrics()

# Results
# ===== 1회 요청 =====
# 응답 시간 : 0.987
# 입력 토큰 : 1668

# Prefix Cache Metrics

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 1857
# Prefix Cache 적중 횟수 : 147
# Prefix Cache 적중률 : 7.92
# KV Cache 사용률 : 0.00

# ===== 2회 요청 =====
# 응답 시간 : 0.831
# 입력 토큰 : 1668

# Prefix Cache Metrics

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 3524
# Prefix Cache 적중 횟수 : 1804
# Prefix Cache 적중률 : 51.19
# KV Cache 사용률 : 0.00

# ===== 3회 요청 =====
# 응답 시간 : 0.815
# 입력 토큰 : 1668

# Prefix Cache Metrics

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 5191
# Prefix Cache 적중 횟수 : 3461
# Prefix Cache 적중률 : 66.67
# KV Cache 사용률 : 0.00

# ===== 4회 요청 =====
# 응답 시간 : 0.811
# 입력 토큰 : 1668

# Prefix Cache Metrics

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 6858
# Prefix Cache 적중 횟수 : 5118
# Prefix Cache 적중률 : 74.63
# KV Cache 사용률 : 0.00