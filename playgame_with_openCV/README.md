### mediapipe를 이용해 손가락 움직임을 인식하여 chrome dinosaur game하는 모델

https://levelup.gitconnected.com/playing-chromes-dinosaur-game-using-opencv-19b3cf9c3636
https://www.youtube.com/watch?v=CJSobYHYDo4

위 두개의 코드를 참고하여 만듬

 - problem: 처음 모델은 컬러를 바탕으로 손을 인식하는 모델이라 환경에 따른 영향을 많이 받아 조작이 쉽지 않았음( 피부색과 비슷한 색을 모두 인식하여 계속 스페이스가 눌리는 사태발생)
 - solution: 그래서 컬러가 아닌 손을 감지하는 mediapipe를 사용하여 인식하니 훨씬 정확도가 높아짐
