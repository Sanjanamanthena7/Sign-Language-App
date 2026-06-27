import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#model path
MODEL_PATH=r"C:\Users\22053\OneDrive\Desktop\example\models\hand_landmarker.task"

#Create a landmark
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)

options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2, running_mode=vision.RunningMode.VIDEO)
landmarker = vision.HandLandmarker.create_from_options(options)

# Live stream
cap=cv2.VideoCapture(0)
time_frame_ms=0
while cap.isOpened():
    success,frame=cap.read()
    if not success:
        break
    frame=cv2.flip(frame,1)
    h,w,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    mp_frame=mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    result=landmarker.detect_for_video(mp_frame,time_frame_ms)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            for landmark in hand_landmarks:
                x=int(landmark.x*w) #changing mediapipe coordinates to pixel coordinates
                y=int(landmark.y*h)
                cv2.circle(frame,(x,y),4,(0,255,0),-1)
    cv2.imshow("Hand Landmark",frame)
    time_frame_ms+=33
    if cv2.waitKey(10) & 0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
