"""
Author: James Villanueva

This file supports the CLI RPS game :)
"""

import random

class RPS:
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
            ("r", "r"): "Tie!",
            ("r", "p"): "You lose!",
            ("r", "s"): "You win!",
            ("p", "r"): "You win!",
            ("p", "p"): "Tie!",
            ("p", "s"): "You lose!",
            ("s", "r"): "You lose!",
            ("s", "p"): "You win!",
            ("s", "s"): "Tie!",
        }

        print(f"CPU chose: {cpuChoice}")
        print(outcomes[(playerChoice, cpuChoice)])

    def main(self) -> None:
        while True:
            self.play()


if __name__ == "__main__":
    RPS().main()
