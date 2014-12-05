from questions import Questions
from dblinker import Dblinker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from connection import Base


class Game(Questions, Dblinker):

    def __init__(self):
        self.questions = Questions()
        self.player1 = Dblinker()

    def calculate_score(self, n):
        return n * n

    def play(self):
        nickname = input("Enter your player name> ")
        print("Welcome, {}! Let the game begin!".format(nickname))
        points_counter = 0
        while True:
            print(self.questions.generate_question())
            correct_answer = self.questions.solve_question()
            player_answer = int(input())
            if player_answer == correct_answer:
                points_counter += 1
                points = (self.calculate_score(points_counter))
                print("Correct!")
            else:
                print("Incorrect! Ending game. You score is: {}".format(points))
                break
            self.player1.update_table(nickname, points)


def main():
    start_choice = Game()
    highscores_choice = Dblinker()

    print(" Welcome to the Do you even math game! Here are your options:\n- start\n- highscores")
    player_input = input()
    if player_input == "highscores":
        highscores_choice.list_highscores()
    elif player_input == "start":
        start_choice.play()
    else:
        "Incorrect command!"

if __name__ == "__main__":
    main()
