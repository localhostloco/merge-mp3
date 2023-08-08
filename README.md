# Audio Merging Project

This project allows you to merge vocals from one audio file with another audio track.

## Dependencies

The main dependencies of this project are:
- `pydub`: For audio manipulation
- `gtts`: For generating text-to-speech (if needed)

Additionally, you'll need to have `ffmpeg` installed, as `pydub` relies on it for audio format conversions.

## Installation

### 1. Clone the Repository
(if you have the project on a repository)

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install FFmpeg
Make sure you have `ffmpeg` installed on your system. If not, you can usually install it via a package manager. For instance, on Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

### 3. Install Python Dependencies

To install the required Python libraries, run:

```bash
pip install -r requirements.txt
```

## Running the Script

1. Ensure your `existing_audio.mp3` and `vocals.mp3` files are in the main directory.
2. Run the script:

```bash
python merge_audio.py
```

3. The merged audio will be saved as `output.mp3`.

## Configuration

You can adjust the merging position by editing the `position` variable in the script. It's set in milliseconds, so for instance, 5000 will overlay the vocals 5 seconds into the existing audio.

---


