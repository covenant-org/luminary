import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import librosa
import pyaudio
import time
import math

# Constants
SAMPLE_RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 3
THRESHOLD_DB = 70

# Load YAMNet model
print("🔄 Loading YAMNet model...")
yamnet_model = hub.load('https://tfhub.dev/google/yamnet/1')
print("✅ YAMNet model loaded.")

# Labels of interest
KEYWORDS = ["scream", "screaming", "yell", "help", "cry", "shout"]

# Load YAMNet class labels
def load_labels():
		import urllib.request
		labels_url = "https://raw.githubusercontent.com/tensorflow/models/master/research/audioset/yamnet/yamnet_class_map.csv"
		labels_path = "yamnet_class_map.csv"
		urllib.request.urlretrieve(labels_url, labels_path)
		with open(labels_path, "r") as f:
				return [line.strip().split(',')[2] for line in f.readlines()[1:]]

labels = load_labels()

# Convert RMS to decibels
def rms_to_db(rms):
		return 20 * np.log10(rms + 1e-6)

# List available microphones
def list_microphones():
		p = pyaudio.PyAudio()
		print("🎤 Available input devices:")
		for i in range(p.get_device_count()):
				info = p.get_device_info_by_index(i)
				if info['maxInputChannels'] > 0:
						print(f"{i}: {info['name']} (Channels: {info['maxInputChannels']})")
		p.terminate()

# Ask user to select input device
list_microphones()
selected_index = int(input("🛠️ Enter the microphone index to use: "))

# Open selected microphone
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
								channels=1,
								rate=SAMPLE_RATE,
								input=True,
								input_device_index=selected_index,
								frames_per_buffer=CHUNK)

print("\n🎙️ Starting help sound detection... Press Ctrl+C to stop.\n")

try:
		while True:
				print("🟡 Listening...")
				frames = []

				for _ in range(0, int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):
						data = stream.read(CHUNK, exception_on_overflow=False)
						frames.append(np.frombuffer(data, dtype=np.int16))

				audio_np = np.hstack(frames).astype(np.float32) / 32768.0

				# Calculate volume
				rms = np.sqrt(np.mean(audio_np ** 2))
				db = rms_to_db(rms)
				bar = "#" * int(max(0, db + 60) // 2)
				print(f"🔊 Volume: {db:.2f} dB [{bar}]")

				# Classify with YAMNet
				scores, embeddings, spectrogram = yamnet_model(audio_np)
				scores_np = scores.numpy().mean(axis=0)
				top_indexes = np.argsort(scores_np)[-10:][::-1]
				top_labels = [(labels[i], scores_np[i]) for i in top_indexes]

				print("🔍 Top detected labels:")
				for label, score in top_labels:
						print(f" - {label}: {score:.2f}")

				match_found = any(label in KEYWORDS for label, _ in top_labels)

				if db >= THRESHOLD_DB and match_found:
						print("\n✅ Help sound detected! Proceed to drop the med-kit.\n")
				else:
						print("❌ No valid help sound detected.")

				time.sleep(1)

except KeyboardInterrupt:
		print("\n⛔ Detection stopped by user.")

finally:
		stream.stop_stream()
		stream.close()
		p.terminate()
