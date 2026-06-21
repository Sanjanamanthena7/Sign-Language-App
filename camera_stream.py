# backend/camera_stream.py

import cv2
import mediapipe as mp

from backend.hand_landmarker import create_hand_landmarker
from backend.gesture_rules import detect_gesture
from backend.drawing_utils import draw_text, draw_landmarks


# Create hand landmarker once
landmarker = create_hand_landmarker()

# Timestamp for VIDEO mode
timestamp = 0


def process_frame(frame):

    global timestamp

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Create MediaPipe Image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    # Detect hand landmarks
    results = landmarker.detect_for_video(
        mp_image,
        timestamp
    )

    # Increment timestamp (~30 FPS)
    timestamp += 33

    # If hand detected
    if results.hand_landmarks:

        # Draw hand skeleton
        frame = draw_landmarks(
            frame,
            results.hand_landmarks
        )

        # Use first hand for gesture recognition
        hand = results.hand_landmarks[0]

        # Detect gesture
        sign = detect_gesture(hand)

        from backend.speaker import speak

        #speak(sign)

        # Draw gesture name
        frame = draw_text(
            frame,
            sign
        )

    return frame