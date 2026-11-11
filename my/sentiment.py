from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
)

review = "삼성전자의 주가는 오늘 5% 변동했다."

response = client.chat.completions.create(
    model=client.models.list().data[0].id,
    messages=[
        {"role": "user", "content": f"Classify sentiment: '{review}'"}
    ],
    extra_body={
        "structured_outputs": {
            "choice": ["positive", "negative", "neutral"]
        }
    },
    temperature=0.0,
)

print(response.choices[0].message.content)