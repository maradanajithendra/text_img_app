import requests
from io import BytesIO

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

def generate_image(api_key, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.content  # return raw image bytes
    else:
        raise Exception(response.text)