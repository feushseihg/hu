#4视频生成
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os
import cv2 as cv
import time
import numpy as np
from mediapipe.framework.formats import landmark_pb2
hand_landmarks=[]

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
# Create a gesture recognizer instance with the video mode:
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
    running_mode=VisionRunningMode.VIDEO,num_hands=2)
recognizer =GestureRecognizer.create_from_options(options)
cap = cv.VideoCapture(0)
x=100
y=100
while True:
    ret, frame = cap.read()
    if not ret:
        break
    color=(0,200,0)
    
    banjing=50 
    # 图片翻转，两个手都可以识别
    frame = cv.flip(frame, 1)
    frame_timestamp_ms = int(time.time() * 1000)
    
    # 转换为MediaPipe图像格式
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    
    # 异步识别手势
    gesture_recognition_result = recognizer.recognize_for_video(mp_image, frame_timestamp_ms)
    
    # 使用最新的识别结果绘制手势
    if gesture_recognition_result:
        for hand_landmarks in gesture_recognition_result.hand_landmarks:
            
            index_finger_tip = hand_landmarks[8]
            index=hand_landmarks[4]  # hand是gesture_recognition_result.hand_landmarks中的元素
# 将归一化坐标转换为屏幕实际像素坐标（需结合图像尺寸）
            h, w,_ = frame.shape  # 图像高度和宽度
            hand_x = int(index_finger_tip.x * w)  # 手部关键点的x坐标（像素）
            hand_y = int(index_finger_tip.y * h) 
            han_x = int(index.x * w)  # 手部关键点的x坐标（像素）
            han_y = int(index.y * h)
            if np.sqrt((hand_x - han_x) **2 + (hand_y - han_y)** 2)<=100:
                distance = np.sqrt((hand_x - x) **2 + (hand_y - y)** 2)
                if distance <= banjing:
                    color=(0, 0, 255)
                    x=hand_x
                    y=hand_y  # 手部在圆形内，改为红色
                # 可添加其他操作
    

            # 转换为proto格式以便绘制
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z)                                             
                 for landmark in hand_landmarks
            ])
            
            # 绘制手部关键点和连接线
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks_proto,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
            
    cv.circle(frame,(x,y),50,color,-1)       # 显示识别出的手势
            
       
    # 显示结果
    cv.imshow("Gesture Recognition", frame)
    
    # 按ESC键退出
    if cv.waitKey(1) & 0xFF == 27:
        break

# 释放资源
cap.release()
cv.destroyAllWindows()
recognizer.close()  # 关闭识别器