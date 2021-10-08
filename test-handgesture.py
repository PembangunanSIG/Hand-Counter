import cv2
import HandTrackingModule as htm


cap = cv2.VideoCapture(1)

detectorTangan = htm.handDetector ( detectionCon=0.75 )
tipIds = [4, 8, 12, 16, 20]

def handButton():
    while True:
        ret, frame = cap.read()
        imgH = detectorTangan.findHands(frame)
        lmList = detectorTangan.findPosition (imgH, draw=False)
        if len ( lmList ) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append ( 1 )
            else:
                fingers.append ( 0 )

            # 4 Fingers
            for id in range ( 1, 5 ):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append ( 1 )
                else:
                    fingers.append ( 0 )

            # print(fingers)
            totalFingers = fingers.count ( 1 )
            print ( totalFingers )

            if totalFingers == 1:
                print('1 Jari')
            if totalFingers == 2:
                print('2 Jari')
            if totalFingers == 3:
                print('3 Jari')
            if totalFingers == 4:
                print('4 Jari')
            if totalFingers == 5:
                print('5 Jari')
            if totalFingers == 0:
                print('0 Jari')
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

handButton()