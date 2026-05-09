import cv2


def drawUI(
    img,
    gameState,
    playerScore,
    computerScore,
    target,
    winnerText,
    lastPlayerNumber,
    lastComputerNumber,
    matchResultText
):

    # STATE DISPLAY
    cv2.putText(
        img,
        f"STATE: {gameState}",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # START SCREEN
    if gameState == "START":

        cv2.putText(
            img,
            "SHOW 2 TO START",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

    # TOSS CHOICE
    elif gameState == "TOSS_CHOICE":

        cv2.putText(
            img,
            "1 = ODD",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            "2 = EVEN",
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

    # TOSS
    elif gameState == "TOSS":

        cv2.putText(
            img,
            "SHOW TOSS NUMBER",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    # ROLE SELECTION
    elif gameState == "ROLE_SELECT":

        cv2.putText(
            img,
            "1 = BOWL",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            "2 = BAT",
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

    # PLAYER BATTING
    elif gameState == "PLAYER_BATTING":

        cv2.putText(
            img,
            "YOU ARE BATTING",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            f"PLAYER SCORE: {playerScore}",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            f"YOU: {lastPlayerNumber}",
            (20, 220),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            f"COMPUTER: {lastComputerNumber}",
            (20, 280),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            matchResultText,
            (20, 340),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # COMPUTER BATTING
    elif gameState == "COMPUTER_BATTING":

        cv2.putText(
            img,
            "COMPUTER BATTING",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            f"COMPUTER SCORE: {computerScore}",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            f"TARGET: {target}",
            (20, 220),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2
        )

        cv2.putText(
            img,
            f"YOU BOWLED: {lastPlayerNumber}",
            (20, 280),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            f"COMPUTER PLAYED: {lastComputerNumber}",
            (20, 340),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            matchResultText,
            (20, 400),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # RESTARTT
    

            # RESTART MENU
    elif gameState == "RESTART":

        cv2.putText(
            img,
            "MATCH OVER",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        cv2.putText(
            img,
            winnerText,
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            img,
            "2 = PLAY AGAIN",
            (20, 260),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            "1 = EXIT",
            (20, 320),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )
        