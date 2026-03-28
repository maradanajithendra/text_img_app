import requests
from PIL import Image
from io import BytesIO

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

def generate_image(api_key, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    # Debug print (optional)
    # print(response.text)

    if response.status_code != 200:
        raise Exception(f"Error generating image: {response.text}")

    image = Image.open(BytesIO(response.content))
    return image
