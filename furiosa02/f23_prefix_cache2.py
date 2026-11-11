# 23-1 카피

from setting import run_once, get_cache_metrics

prefix = "NPU 추론 최적화이 대한 설명입니다." * 150

for i in range(1, 5):
    print(f"\n===== {i}회 요청 =====")
    prompt = prefix + f"\n질문 {i}: KV Cache란?"

    before = get_cache_metrics()    # 요청 전 캐시 상태
    result = run_once(prompt, 100)
    after = get_cache_metrics() # 요청 후 캐시 상태

    # 이번 요청에서 증가한 횟수
    hits = after["hits"] - before["hits"]
    queries = after["queries"] - before["queries"]

    if queries > 0:
        hit_rate = hits / queries * 100
    else:
        hit_rate = 0

    print(f"\n===== {i}회 요청결과 =====")
    print("응답 시간 :", round(result["elapsed"], 3))
    print("입력 토큰 :", result["input_tokens"])
    print("이번 조회 횟수 :", int(queries))
    print("이번 적중 횟수 :", int(hits))
    print("이번 적중률 :", round(hit_rate,  2), "%")

# Results
# ===== 1회 요청 =====

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 13526
# Prefix Cache 적중 횟수 : 11786
# Prefix Cache 적중률 : 87.14
# KV Cache 사용률 : 0.00

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 15193
# Prefix Cache 적중 횟수 : 13453
# Prefix Cache 적중률 : 88.55
# KV Cache 사용률 : 0.00

# ===== 1회 요청결과 =====
# 응답 시간 : 0.843
# 입력 토큰 : 1668
# 이번 조회 횟수 : 1667
# 이번 적중 횟수 : 1667
# 이번 적중률 : 100.0 %

# ===== 2회 요청 =====

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 15193
# Prefix Cache 적중 횟수 : 13453
# Prefix Cache 적중률 : 88.55
# KV Cache 사용률 : 0.00

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 16860
# Prefix Cache 적중 횟수 : 15120
# Prefix Cache 적중률 : 89.68
# KV Cache 사용률 : 0.00

# ===== 2회 요청결과 =====
# 응답 시간 : 0.83
# 입력 토큰 : 1668
# 이번 조회 횟수 : 1667
# 이번 적중 횟수 : 1667
# 이번 적중률 : 100.0 %

# ===== 3회 요청 =====

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 16860
# Prefix Cache 적중 횟수 : 15120
# Prefix Cache 적중률 : 89.68
# KV Cache 사용률 : 0.00

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 18527
# Prefix Cache 적중 횟수 : 16787
# Prefix Cache 적중률 : 90.61
# KV Cache 사용률 : 0.00

# ===== 3회 요청결과 =====
# 응답 시간 : 0.848
# 입력 토큰 : 1668
# 이번 조회 횟수 : 1667
# 이번 적중 횟수 : 1667
# 이번 적중률 : 100.0 %

# ===== 4회 요청 =====

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 18527
# Prefix Cache 적중 횟수 : 16787
# Prefix Cache 적중률 : 90.61
# KV Cache 사용률 : 0.00

# ====== Furiosa NPU Cache 상태 ======
# Prefix Cache 조회 횟수 : 20194
# Prefix Cache 적중 횟수 : 18454
# Prefix Cache 적중률 : 91.38
# KV Cache 사용률 : 0.00

# ===== 4회 요청결과 =====
# 응답 시간 : 0.823
# 입력 토큰 : 1668
# 이번 조회 횟수 : 1667
# 이번 적중 횟수 : 1667
# 이번 적중률 : 100.0 %