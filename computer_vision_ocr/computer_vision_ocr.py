# -----------------------------------------------------------------------------
# Script Name: computer_vision_ocr.py
# Description: Use Azure Computer Vision
# Author: ChatGPT with De'modori Gatsuo
# Created Date: 2023.09.30
# -----------------------------------------------------------------------------

import os
import requests

COMPUTER_VISION_URL = os.environ['COMPUTER_VISION_URL']
COMPUTER_VISION_KEY = os.environ['COMPUTER_VISION_KEY']

# get image from line
# USE message id
def get_image_content_from_line(image_id):
    headers = {
        'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'
    }
    response = requests.get(f'https://example_image_url_{image_id}', headers=headers)
    return response.content

# execute OCR
def extract_text_from_image(image_data):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': COMPUTER_VISION_KEY
    }
    response = requests.post(COMPUTER_VISION_URL, headers=headers, data=image_data)
    data = response.json()
    return data['readResult']['content']

if __name__ == "__main__":
    image_id = "000000" # dummy
    image_data = get_image_content_from_line(image_id)
    extract_text = extract_text_from_image(image_data)
    print(extract_text)