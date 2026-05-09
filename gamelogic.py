import random


# START GAME
def startGame(acceptedNumber, gameState):

    if gameState == "START":

        if acceptedNumber == 2:

            print("GAME STARTED")

            gameState = "TOSS_CHOICE"

        elif acceptedNumber == 0:

            print("EXIT")

    return gameState


# TOSS CHOICE
def tossChoice(acceptedNumber, gameState):

    playerChoice = ""

    if gameState == "TOSS_CHOICE":

        if acceptedNumber == 1:

            playerChoice = "ODD"

            print("PLAYER CHOSE ODD")

            gameState = "TOSS"

        elif acceptedNumber == 2:

            playerChoice = "EVEN"

            print("PLAYER CHOSE EVEN")

            gameState = "TOSS"

    return gameState, playerChoice


# TOSS RESULT
def tossResult(
    acceptedNumber,
    playerChoice,
    gameState
):

    tossWinner = ""

    computerNumber = random.randint(0, 4)

    if gameState == "TOSS":

        playerNumber = acceptedNumber

        total = playerNumber + computerNumber

        print("PLAYER:", playerNumber)
        print("COMPUTER:", computerNumber)
        print("TOTAL:", total)

        # EVEN
        if total % 2 == 0:

            result = "EVEN"

        else:

            result = "ODD"

        print("RESULT:", result)

        # Decide toss winner
        if result == playerChoice:

            tossWinner = "PLAYER"

        else:

            tossWinner = "COMPUTER"

        print("TOSS WINNER:", tossWinner)

        gameState = "ROLE_SELECT"

    return gameState, tossWinner, computerNumber


# ROLE SELECTION
def roleSelection(
    acceptedNumber,
    tossWinner,
    gameState
):

    playerRole = ""
    computerRole = ""

    if gameState == "ROLE_SELECT":

        if tossWinner == "PLAYER":

            # 2 = Bat
            if acceptedNumber == 2:

                playerRole = "BAT"

                computerRole = "BOWL"

            # 1 = Bowl
            elif acceptedNumber == 1:

                playerRole = "BOWL"

                computerRole = "BAT"

        else:

            # Computer random role
            computerRole = random.choice(["BAT", "BOWL"])

            if computerRole == "BAT":

                playerRole = "BOWL"

            else:

                playerRole = "BAT"

        print("PLAYER ROLE:", playerRole)
        print("COMPUTER ROLE:", computerRole)

        # Decide first innings
        if playerRole == "BAT":

            gameState = "PLAYER_BATTING"

        else:

            gameState = "COMPUTER_BATTING"

    return gameState, playerRole, computerRole


# PLAYER 1 INNINGS
def playerBatting(
    playerNumber,
    computerNumber,
    playerScore,
    gameState
):

    out = False
    target = 0

    if gameState == "PLAYER_BATTING":

        # OUT
        if playerNumber == computerNumber:

            print("PLAYER 1 OUT")

            out = True

            target = playerScore + 1

            gameState = "COMPUTER_BATTING"

        else:

            playerScore += playerNumber

            print("PLAYER 1 SCORE:", playerScore)

    return gameState, playerScore, target, out


# PLAYER 2 INNINGS
def computerBatting(
    playerNumber,
    computerNumber,
    computerScore,
    target,
    gameState
):

    winnerText = ""

    if gameState == "COMPUTER_BATTING":

        # OUT
        if playerNumber == computerNumber:

            print("PLAYER 2 OUT")

            # Decide winner
            if computerScore >= target:

                winnerText = "PLAYER 2 WINS"

            else:

                winnerText = "PLAYER 1 WINS"

            gameState = "RESTART"

        else:

            computerScore += computerNumber

            print("PLAYER 2 SCORE:", computerScore)

            # Chase complete
            if computerScore >= target:

                winnerText = "PLAYER 2 WINS"

                gameState = "RESTART"

    return gameState, computerScore, winnerText
# RESTART GAME

def restartGame(
    acceptedNumber,
    gameState
):

    if gameState == "RESTART":

        # 2 = YES
        if acceptedNumber == 2:

            gameState = "START"

        # 1 = NO
        elif acceptedNumber == 1:

            gameState = "EXIT"

    return gameState