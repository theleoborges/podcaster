from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import numpy as np
import sys

if len(sys.argv) != 2:
    print("Usage: python main.py <file_path>")
    sys.exit(1)
script_path = sys.argv[1]

script = ""
with open(script_path) as f:
    script = f.read()

# Cleanup script
script = script.strip().split("\n")
script = [s.strip() for s in script if s]

# download and load all bark models
preload_models()

# Setup speaker voices
speakers = {"Jane": "v2/en_speaker_9", "Matt": "v2/en_speaker_2"}

pieces = []
silence = np.zeros(int(0.5*SAMPLE_RATE))
for line in script:
    speaker, text = line.split(": ")
    audio_array = generate_audio(text, history_prompt=speakers[speaker], )
    pieces += [audio_array, silence.copy()]

audio_array = np.concatenate(pieces)

# save audio to disk
write_wav("podcast.wav", SAMPLE_RATE, audio_array)
print("Saved audio to 'podcast.wav'")
  
