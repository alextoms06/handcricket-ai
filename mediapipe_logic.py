import cv2
import mediapipe as mp


# Initialize MediaPipe Hands
mpHands = mp.solutions.hands

hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Drawing utility
mpDraw = mp.solutions.drawing_utils


def detectGesture(img):

    acceptedNumber = -1

    # Convert BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process image
    results = hands.process(imgRGB)

    # If hands detected
    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            # Draw landmarks
            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

            # Store landmarks
            lmList = []

            for id, lm in enumerate(handLms.landmark):

                h, w, c = img.shape

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append([id, cx, cy])

                # Draw landmark points
                cv2.circle(
                    img,
                    (cx, cy),
                    5,
                    (255, 0, 255),
                    cv2.FILLED
                )

            # Fingertip IDs
            tipIds = [4, 8, 12, 16, 20]

            fingers = []

            # Ignore thumb for stability
            for i in range(1, 5):

                if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:

                    fingers.append(1)

                else:

                    fingers.append(0)

            # Count fingers
            number = fingers.count(1)

            acceptedNumber = number

            # Display number
            cv2.putText(
                img,
                f"Number: {number}",
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

    return img, acceptedNumber