from furiosa01.setting import get_llm

llm = get_llm(
    max_tokens=1000,
    temperature=2,
    top_p=1
)

response = llm.invoke("NPU와 GPU의 차이점을 설명해줘.")

print(response.content)