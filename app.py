from pydub import AudioSegment

# Paths to your existing audio files
existing_audio_file = "track.mp3"
vocals_file = "afirmaciones.mp3"

# Load the existing audio files
existing_audio = AudioSegment.from_mp3(existing_audio_file)
vocals_audio = AudioSegment.from_mp3(vocals_file)

# Overlay the vocals onto the existing audio at a specific position (milliseconds)
# You can adjust the position as needed
position = 0 # Starts the vocals at 5 seconds into the existing audio
merged_audio = existing_audio.overlay(vocals_audio, position=position)

# Export the merged audio
merged_audio.export("output.mp3", format="mp3")

print("Audio merged and saved as output.mp3")