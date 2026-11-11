from furiosa_llm import LLM, SamplingParams

with LLM("furiosa-ai/Meta-Llama-3.1-8B-Instruct-FP8-dynamic") as llm:
    params = SamplingParams(min_tokens=10, max_tokens=1000, top_p=0.3, top_k=100)

    message = [{"role":"user", "content":"오늘 삼성 주가 알려줘."}]
    prompt = llm.tokenizer.apply_chat_template(message, tokenize=False)

    response = llm.generate([prompt], params)

    print(response[0].outputs[0].text)