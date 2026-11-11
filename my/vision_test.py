from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
)

response = client.chat.completions.create(
    model="furiosa-ai/Qwen3-VL-2B-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"
                    },
                },
                {
                    "type": "text",
                    "text": "Explain what you see in this image.",
                },
            ],
        }
    ],
    max_tokens=256,
)

print(response.choices[0].message.content)