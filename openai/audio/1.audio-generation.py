from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "./audio-synthetic/Korean-speech.mp3"

# Convert text into speech
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="안영하세요요."
)
response.stream_to_file(speech_file_path)
print("resposne: ", response)