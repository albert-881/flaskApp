from flask import Flask, render_template, request
import random

flaskfinalproject = Flask(__name__)

class WordleGame:
    def __init__(self, secret_word, max_guesses):
        self.secret_word = secret_word
        self.max_guesses = max_guesses
        self.guessed_letters = []
        self.valid_letters = "abcdefghijklmnopqrstuvwxyz"
        self.guesses_left = max_guesses

    def play(self, guess):
        message = ""
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "-"
        if guess not in self.valid_letters:
            message = "Invalid guess. Please guess a letter."
        elif guess in self.guessed_letters:
            message = "You already guessed that letter."
        else:
            self.guessed_letters.append(guess)
            if guess in self.secret_word:
                message = "Good guess!"
            else:
                message = "Sorry, that letter is not in the word."
                self.guesses_left -= 1
        if display_word == self.secret_word:
            return {"message": "Congratulations! You won!", "game_over": True}
        elif self.guesses_left == 0:
            return {"message": "Sorry, you lost. The word was " + self.secret_word, "game_over": True}
        else:
            message += " You have " + str(self.guesses_left) + " guesses left."
            return {"message": message, "game_over": False, "display_word": display_word}

class EasyWordleGame(WordleGame):
    def __init__(self):
        wordlist = ["cat", "dog", "hat", "red", "pen"]
        secret_word = random.choice(wordlist)
        super().__init__(secret_word, 10)

class MediumWordleGame(WordleGame):
    def __init__(self):
        wordlist = ["apple", "banana", "cherry", "orange", "grape"]
        secret_word = random.choice(wordlist)
        super().__init__(secret_word, 8)

class HardWordleGame(WordleGame):
    def __init__(self):
        wordlist = ["python", "java", "c++", "assembly", "csharp"]
        secret_word = random.choice(wordlist)
        super().__init__(secret_word, 6)

@flaskfinalproject.route("/", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        easy_game = EasyWordleGame()
        return render_template("wordle.html", display_word="-" * len(easy_game.secret_word), message="Welcome to Wordle! You have 10 guesses to guess the word.", game_over=False)
    else:
        guess = request.form["guess"].lower()
        display_word = request.form["display_word"]
        message = request.form["message"]
        game_over = request.form["game_over"] == "True"
        easy_game = EasyWordleGame()  # Define the object in the POST method
        if not game_over:
            if len(guess) == 1:
                result = easy_game.play(guess)
                display_word = result["display_word"]
                message = result["message"]
                game_over = result["game_over"]
        return render_template("wordle.html", display_word=display_word, message=message, game_over=game_over)

if __name__ == "__main__":
    flaskfinalproject.run(debug=True, port=3000)
    flaskfinalproject.config['DEBUG'] = True
    
    # 
    