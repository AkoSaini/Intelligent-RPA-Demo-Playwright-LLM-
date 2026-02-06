import os
import json
import requests
from dotenv import load_dotenv

# Load API credentials from .env file
load_dotenv()
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_URL = os.getenv("LLM_API_URL")


def extract_fields(text: str) -> dict:
    """
    Sends unstructured text to an LLM and returns structured fields:
    name, account_number, request_type, notes
    """

    if not LLM_API_KEY or not LLM_API_URL:
        raise RuntimeError("Missing LLM API configuration in .env")

    # Instructions telling the LLM exactly what to extract
    system_prompt = (
        "Extract the following fields from the text:\n"
        "name, account_number, request_type, notes.\n"
        "Return ONLY valid JSON with exactly these keys."
    )

    # OpenAI-compatible chat payload
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        "temperature": 0.0,
    }

    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json",
    }

    # Call the LLM API
    r = requests.post(LLM_API_URL, headers=headers, json=payload, timeout=30)

    if r.status_code != 200:
        raise RuntimeError(f"LLM API error {r.status_code}:\n{r.text}")

    data = r.json()

    # Extract model response text
    content = data["choices"][0]["message"]["content"]

    # Convert JSON string to Python dict
    if isinstance(content, dict):
        return content

    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1].strip()
        if content.lower().startswith("json"):
            content = content[4:].strip()

    return json.loads(content)


if __name__ == "__main__":
    sample_text = (
        "Hi, this is John Smith. My account number is 45678. "
        "I moved to Dallas and need my address updated. "
        "Please note this on my account."
    )

    print(extract_fields(sample_text))
