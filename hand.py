import cv2
import time
import random

from mediapipe_logic import detectGesture

from ui import drawUI

from gamelogic import (
    startGame,
    tossChoice,
    tossResult,
    roleSelection,
    playerBatting,
    computerBatting,
    restartGame     
)

# Webcam
cap = cv2.VideoCapture(0)

# FPS
prevTime = 0

# Gesture stabilization
prevNumber = -1
stableFrames = 0
acceptedNumber = -1

# Cooldown
gestureCooldown = 0

# Game variables
gameState = "START"

playerChoice = ""

playerScore = 0
computerScore = 0

target = 0

winnerText = ""

tossWinner = ""

playerRole = ""
computerRole = ""

lastPlayerNumber = 0
lastComputerNumber = 0

matchResultText = ""

while True:

    success, img = cap.read()

    if not success:

        print("Camera not detected")
        break

    # Flip webcam
    img = cv2.flip(img, 1)

    # Cooldown
    if gestureCooldown > 0:

        gestureCooldown -= 1

    # Detect gesture
    img, number = detectGesture(img)

    # Stabilization
    if number != -1:

        if number == prevNumber:

            stableFrames += 1

        else:

            stableFrames = 0

        prevNumber = number

        # Accept gesture
        if stableFrames > 15 and gestureCooldown == 0:

            oldState = gameState

            acceptedNumber = number

            print("ACCEPTED:", acceptedNumber)

            # START
            if gameState == "START":

                gameState = startGame(
                    acceptedNumber,
                    gameState
                )

            # TOSS CHOICE
            elif gameState == "TOSS_CHOICE":

                gameState, playerChoice = tossChoice(
                    acceptedNumber,
                    gameState
                )

            # TOSS
            elif gameState == "TOSS":

                gameState, tossWinner, computerNumber = tossResult(
                    acceptedNumber,
                    playerChoice,
                    gameState
                )

            # ROLE SELECTION
            elif gameState == "ROLE_SELECT":

                gameState, playerRole, computerRole = roleSelection(
                    acceptedNumber,
                    tossWinner,
                    gameState
                )

            # PLAYER BATTING
            elif gameState == "PLAYER_BATTING":

                computerNumber = random.randint(0, 4)

                lastPlayerNumber = acceptedNumber
                lastComputerNumber = computerNumber

                gameState, playerScore, target, out = playerBatting(
                    acceptedNumber,
                    computerNumber,
                    playerScore,
                    gameState
                )

                if acceptedNumber == computerNumber:

                    matchResultText = "OUT"

                else:

                    matchResultText = f"+{acceptedNumber} RUNS"

            # COMPUTER BATTING
            elif gameState == "COMPUTER_BATTING":

                computerNumber = random.randint(0, 4)

                lastPlayerNumber = acceptedNumber
                lastComputerNumber = computerNumber

                gameState, computerScore, winnerText = computerBatting(
                    acceptedNumber,
                    computerNumber,
                    computerScore,
                    target,
                    gameState
                )

                if acceptedNumber == computerNumber:

                    matchResultText = "COMPUTER OUT"

                else:

                    matchResultText = f"COMPUTER +{computerNumber}"
                    
                        # RESTART MENU
            elif gameState == "RESTART":

                gameState = restartGame(
                    acceptedNumber,
                    gameState
                )

                # Reset scores if restarting
                if gameState == "START":

                    playerScore = 0
                    computerScore = 0

                    target = 0

                    winnerText = ""

                    matchResultText = ""

                    playerChoice = ""

                    tossWinner = ""
            
                        # EXIT GAME
            elif gameState == "EXIT":

                cap.release()
                cv2.destroyAllWindows()
                exit()

            # State change delay
            if oldState != gameState:

                stableFrames = 0
                prevNumber = -1
                acceptedNumber = -1

                cv2.imshow("Hand Cricket", img)

                cv2.waitKey(1)

                time.sleep(1.5)

            # Cooldown
            gestureCooldown = 40

    # FPS
    currTime = time.time()

    fps = 1 / (currTime - prevTime)

    prevTime = currTime

    # FPS display
    cv2.putText(
        img,
        f"FPS: {int(fps)}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Draw UI
    drawUI(
        img,
        gameState,
        playerScore,
        computerScore,
        target,
        winnerText,
        lastPlayerNumber,
        lastComputerNumber,
        matchResultText
    )

    # Show window
    cv2.imshow("Hand Cricket", img)

    # Exit
    if cv2.waitKey(1) & 0xFF == 27:

        break

# Release
cap.release()

cv2.destroyAllWindows()