import requests
import base64


def ask_vision(image_path, prompt):
    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "model": "qwen/qwen2.5-vl-7b",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        "temperature": 0.2,
        "max_tokens": 500
    }

    response = requests.post(
        "http://127.0.0.1:1234/v1/chat/completions",
        json=payload
    )
    if response.status_code != 200:
        print("Vision API Error:", response.text)

    result = response.json()
    message = result["choices"][0]["message"]

    answer = message.get("content", "")
    reasoning = message.get("reasoning_content", "")

    final_text = answer if str(answer).strip() else reasoning

    return final_text

def classify_image(image_path):
    prompt = """
Reply with EXACTLY one word.

YES = image contains graph/chart/plot with numeric data, bars, lines, axes
NO = normal image, logo, screenshot, product photo, illustration

Answer only YES or NO.
"""

    result = ask_vision(image_path, prompt).strip().upper()

    if result.startswith("YES"):
        return "graph"

    return "photo"