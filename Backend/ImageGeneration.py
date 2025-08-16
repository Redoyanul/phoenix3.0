from huggingface_hub import InferenceClient
from PIL import Image
from dotenv import get_key
import os
from time import sleep

# Load API key from .env file
API_KEY = get_key(".env", "HuggingFaceAPIKey")

# Define Constants
FOLDER_PATH = r"Data"
IMAGE_STATUS_FILE = r"Frontend\Files\ImageGeneration.data"

# Initialize Hugging Face Inference Client
client = InferenceClient(
    provider="together",
    api_key=API_KEY
)

def open_images(prompt):
    """ Opens generated images based on the given prompt. """
    formatted_prompt = prompt.replace(" ", "_")
    files = [os.path.join(FOLDER_PATH, f"{formatted_prompt}{i}.jpg") for i in range(1, 5)]

    for image_path in files:
        try:
            with Image.open(image_path) as img:
                print(f"Opening Image: {image_path}")
                img.show()
                sleep(1)
        except IOError as e:
            print(f"Unable to open {image_path}: {e}")

def generate_images(prompt):
    """ Generate images using Hugging Face's InferenceClient. """
    formatted_prompt = prompt.replace(" ", "_")

    for i in range(1, 5):  # Generate 4 images
        try:
            image = client.text_to_image(
                prompt,
                model="stabilityai/stable-diffusion-xl-base-1.0"
            )
            
            image_path = os.path.join(FOLDER_PATH, f"{formatted_prompt}{i}.jpg")
            image.save(image_path)
            print(f"Image saved: {image_path}")

        except Exception as e:
            print(f"Error generating image {i}: {e}")

def generate_and_open_images(prompt):
    """ Runs the image generation and opens them. """
    generate_images(prompt)
    open_images(prompt)

if __name__ == "__main__":
    while True:
        try:
            if not os.path.exists(IMAGE_STATUS_FILE):
                print(f"File not found: {IMAGE_STATUS_FILE}")
                break

            with open(IMAGE_STATUS_FILE, "r") as f:
                data = f.read().strip()

            if not data:
                sleep(1)
                continue

            prompt, status = data.split(",")

            if status.strip().lower() == "true":
                print("Generating Images...")
                generate_and_open_images(prompt)

                with open(IMAGE_STATUS_FILE, "w") as f:
                    f.write("False, False")
                
                break  # Exit after generating images

            sleep(1)

        except Exception as e:
            print(f"Error: {e}")
            sleep(1)
