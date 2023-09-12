import cv2
import os
from pathlib import Path

CLIP_DIR = '/path to clip folder/'
FRAME_DIR = '/path to the folder to save frames/'
SKIP_FRAMES = 50	#No. of frames to skip

# Get clip list
clips = [f for f in os.listdir(CLIP_DIR) if f.endswith('.mp4')]

for clip in clips:

    # Get clip name and path
    clip_name = Path(clip).stem
    clip_path = os.path.join(CLIP_DIR, clip)

    # Make folder for frames
    frame_folder = os.path.join(FRAME_DIR, clip_name)
    os.makedirs(frame_folder, exist_ok=True)

    # Open clip
    cap = cv2.VideoCapture(clip_path)

    # Get total frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()

        # Break if end of frames
        if not ret:
            break

        # Extract and save frames
        if count % SKIP_FRAMES == 0:
            frame_name = f"{clip_name}_{count}.jpg"
            frame_path = os.path.join(frame_folder, frame_name)
            print(frame_path)
            cv2.imwrite(frame_path, frame)

        count += 1

    # Check for last frame
    if count >= total_frames:
        print("Reached end of clip", clip)
        break

print("Processed all clips successfully.")
