# Video Summarizaer

pip install -r requirements.txt
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128

ngc config set
ngc registry model download-version "nvidia/vila_vision_language_model:1.5.3b" --dest ./models
