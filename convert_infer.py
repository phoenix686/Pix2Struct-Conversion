# Install dependencies
import subprocess

try:
    subprocess.run(["pip", "install", "transformers", "pillow", "tqdm","optimum[exporters]"], check=True)
    print("Dependencies installed successfully.")
except subprocess.CalledProcessError:
    print("Error installing dependencies.")

# Import libraries
import argparse
import requests
from PIL import Image
from transformers import Pix2StructForConditionalGeneration, Pix2StructProcessor
from tqdm import tqdm  # Adding tqdm for progress tracking

# Argument parsing
parser = argparse.ArgumentParser(description="Run Pix2Struct model on an image with a question.")
parser.add_argument("--image", required=True, help="Path to the input image.")
parser.add_argument("--question", required=True, help="The question to ask about the image.")
args = parser.parse_args()

# Download the model
model = Pix2StructForConditionalGeneration.from_pretrained("google/pix2struct-docvqa-base")
processor = Pix2StructProcessor.from_pretrained("google/pix2struct-docvqa-base")
print("Downloaded the model")

# Run inference on Huggingface model
image = Image.open(args.image)
inputs = processor(images=image, text=args.question, return_tensors="pt")

predictions = model.generate(**inputs, max_new_tokens=200)
decoded_prediction = processor.decode(predictions[0], skip_special_tokens=True)
print("Output")
print(decoded_prediction)

# Convert to ONNX
try:
    subprocess.run(
        [
            "optimum-cli",
            "export",
            "onnx",
            "--model",
            "google/pix2struct-docvqa-base",
            "model/"
        ],
        check=True
    )
    print("Model exported to ONNX successfully.")
except subprocess.CalledProcessError:
    print("Error exporting the model to ONNX.")
