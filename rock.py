import random

class RockPaperScissors:
    commands = {'!exit', '!rating'}

    def __init__(self, file_name = "rating.txt"):
        self.game_fig = {"rock":0, "paper":1, "scissors":2}
        self.file_name = file_name
        self.player_choice = ""
        self.player_name = ""
        self.player_score = 0
        self.game_run = True

    def set_player_choice(self):
        self.player_choice = input()

    def set_player_name(self):
        self.player_name = input("Enter your name: ")
        print(f"Hello, {self.player_name}")

    def set_player_score(self, value):
        self.player_score = value

    def read_player_score(self):
        with open(self.file_name, "r") as file:
            for line in file:
                line = line.split()
                if line[0] == self.player_name:
                    self.player_score = int(line[1])
                    break

    def set_game_figure(self):
        figures = input()
        self.game_fig = self.game_fig if not figures else {name: i for i, name in enumerate(figures.split(","))}
        print("Okay, let's start") 

    def match(self):
        pc_choice = random.choice(list(self.game_fig.keys()))
        result = (self.game_fig[self.player_choice] - self.game_fig[pc_choice]) % len(self.game_fig)
        if result == 0:
            print(f"There is a draw({self.player_choice})")
            return 50
        if result > len(self.game_fig) / 2:
            print(f"Sorry, but computer chose {pc_choice}")
            return 0
        print(f"Well done. Computer chose {pc_choice} and failed")
        return 100


    def do_command(self, commands):
        if commands == "!exit":
            self.game_run = False
        elif commands == "!rating":
            print(f"Your rating: {self.player_score}")

    def check_and_run(self):
        while self.game_run:
            self.set_player_choice()
            if self.player_choice in self.game_fig:
                score = self.player_score + self.match()
                self.set_player_score(score)
            elif self.player_choice in RockPaperScissors.commands:
                self.do_command(self.player_choice)
            else:
                print("Invalid input")
        print("Bye!")

    def main(self):
        self.set_player_name()
        self.read_player_score()
        self.set_game_figure()
        self.check_and_run()

if __name__ == "__main__":
    RockPaperScissors().main()