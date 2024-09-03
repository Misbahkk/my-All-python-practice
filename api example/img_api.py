import io
import openai
import requests
import PIL
from PIL import Image

openai.api_key = "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"

def genrate_image(text):
    response = openai.Image.create(
        prompt = text,
        n = 1,
        size = '512x512'
    )
    image_url = response.data[0]['url']
    image_content = requests.get(image_url).content
    image = Image.open(io.BytesIO(image_content))
    image.show()
prompt = input("ENter your Prompt to genrate the image: ")
genrate_image(prompt)