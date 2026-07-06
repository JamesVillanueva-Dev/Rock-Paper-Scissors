"""
Author: James Villanueva

This file supports the CLI RPS game :)
"""

import random

WIN_MESSAGE = "You win!"
LOSE_MESSAGE = "You lose!"
TIE_MESSAGE = "Tie!"

class RPS:
    def __init__(self):
        self.playerScore = 0
        self.cpuScore = 0

    def play(self):
        choices = ["r", "p", "s"]
        print("What do you choose? (R, P, S)")

        inputValid = False
        while not inputValid:
            playerChoice = input().lower()
            if playerChoice in ("r", "p", "s"):
                inputValid = True
            else:
                print("Please put a valid input: (R, P, S)")

        cpuChoice = choices[random.randint(0, len(choices) - 1)]

        outcomes = {
            ("r", "r"): TIE_MESSAGE,
            ("r", "p"): LOSE_MESSAGE,
            ("r", "s"): WIN_MESSAGE,
            ("p", "r"): WIN_MESSAGE,
            ("p", "p"): TIE_MESSAGE,
            ("p", "s"): LOSE_MESSAGE,
            ("s", "r"): LOSE_MESSAGE,
            ("s", "p"): WIN_MESSAGE,
            ("s", "s"): TIE_MESSAGE,
        }

        result = outcomes[(playerChoice, cpuChoice)]
        print(f"CPU chose: {cpuChoice}")
        print(result)
        if result == WIN_MESSAGE:
            self.playerScore += 1
        if result == LOSE_MESSAGE:
            self.cpuScore += 1

        print(f"Score-> Player: {self.playerScore} CPU: {self.cpuScore} \n")

    def main(self) -> None:
        while True:
            self.play()


if __name__ == "__main__":
    RPS().main()
