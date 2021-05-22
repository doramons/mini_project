
import cv2
import mediapipe as mp

# 관절그리는 도구
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 웹캠 켜기
cap = cv2.VideoCapture(0)

# module = Module()

with mp_hands.Hands( #손가락 인식 모델 초기화
    max_num_hands = 1, # 최대 몇개의 손을 인식할건지
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as hands:
    
    while cap.isOpened():
        success, image = cap.read()
        if not success: # 성공하지 못하면 다음 프레임으로
            continue
            
        # 성공하면 밑에꺼 실행
        image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB) # mediapipe는 rgb를 사용함
        result = hands.process(image)
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # cv로 출력해야하므로 다시 bgr로 바꿔줌
        
        if result.multi_hand_landmarks: # 손이 인식되면 밑 코드가 실행됨
            for hand_landmarks in result.multi_hand_landmarks: # 여러개 손이 동시에 검출될 경우 하나씩 불러와서 처리
                thumb = hand_landmarks.landmark[4] # 엄지손가락 인덱스 4 / 손가락 좌표(x,y)를 불러옴
                index = hand_landmarks.landmark[8] # 검지손가락 인덱스가 8번
                
                diff = abs(index.x - thumb.x) # 좌표의 값의 (0~1) 이므로 차도 1이하임
                
                volume = int(diff*500)
                
                # module.motor.angle(volume) # 각도 제어
                # 엄지 검지 간격이 작으면 0에 가까워져서 모터의 각도가 0에 가까워짐
                # 간격 커지면 모터 각도도 커짐
                
                cv2.putText(
                    image, text = 'Volume: %d' %volume, org=(10,30),
                    fontFace = cv2.Font_HERSHEY_SIMPLEX, fontScale = 1,
                    color = 255, thickness=2)
                
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                
        cv2.imshow('image',image)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()