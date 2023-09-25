import envs
import requests


def ask(question: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {envs.OPENAI_API_KEY}'
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}],
    }
    response = requests.post(url=url, headers=headers, json=payload).json()

    return "\n"+response['choices'][0]['message']['content']
