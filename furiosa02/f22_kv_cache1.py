from setting import run_once

short_prompt = "NPU란 무엇인가?"
long_prompt = (
    "NPU는 인공지능 연산을 가속하는 프로세서다." * 100
) + "위 내용을 요약해줘."

tests = [
    ("짧은 입력", short_prompt, 80),
    ("긴 입력", long_prompt, 80),
    ("긴 입력과 긴 출력", long_prompt, 400)
]

for name, prompt, max_tokens in tests:
    results = run_once(prompt, max_tokens)

    print(f"\n실험: {name}")
    print("입력 토큰: ", results["input_tokens"])
    print("출력 토큰: ", results["output_tokens"])
    print("소요 시간: ", results["elapsed"])
    input("서버 KV Cache 사용을 확인하고 싶다 Enter...")

# Results
# 실험: 짧은 입력
# 입력 토큰:  15
# 출력 토큰:  80
# 소요 시간:  0.6641698116436601
# 서버 KV Cache 사용을 확인하고 싶다 Enter...

# 실험: 긴 입력
# 입력 토큰:  1817
# 출력 토큰:  80
# 소요 시간:  0.6588941281661391
# 서버 KV Cache 사용을 확인하고 싶다 Enter...

# 실험: 긴 입력과 긴 출력
# 입력 토큰:  1817
# 출력 토큰:  163
# 소요 시간:  1.3668481302447617
# 서버 KV Cache 사용을 확인하고 싶다 Enter...