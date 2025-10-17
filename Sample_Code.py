import requests
import os
import dotenv
dotenv.load_dotenv() 

def test_euron():
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('Euron_Api_Key')}"
    }
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "HI.Myself Sandeep Srinivasan. I am a software developer."}
        ],
        "model": "gpt-4.1-nano",
        "max_tokens": 1000,
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        print("✅ Euron Response:", data.get("choices", [{}])[0].get("message", {}).get("content", "No response"))
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    test_euron()
