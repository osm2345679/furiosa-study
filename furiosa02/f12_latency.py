from setting import get_llm
import time

llm = get_llm(max_tokens=500)

prompt = "NPU의 특징을 말해줘."

times = []
for i in range(5):
    start = time.perf_counter()

    response = llm.invoke(prompt)

    end = time.perf_counter()

    elasped = end - start

    times.append(elasped)
    print(i + 1, "회:", round(elasped, 2), "초")

average = sum(times) / len(times)

print("평균 응답 시간:", round(average, 2), "초")

# Results
# 1 회: 4.03 초
# 2 회: 4.01 초
# 3 회: 4.0 초
# 4 회: 4.05 초
# 5 회: 4.03 초
# 평균 응답 시간: 4.02 초