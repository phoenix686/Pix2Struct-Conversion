#install dependencies
import subprocess

try:
    subprocess.run(["pip", "install", "transformers", "pillow", "tqdm","optimum[exporters]"], check=True)
    print("Dependencies installed successfully.")
except subprocess.CalledProcessError:
    print("Error installing dependencies.")

#conversion to onnx

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