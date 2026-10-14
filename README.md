# 🎮 Hangman Game Using Python

## 📌 Project Overview

The Hangman Game is a simple, interactive, console-based word-guessing game developed using Python. This project is created as part of the **CodeAlpha Python Programming Internship**.

In this game, the computer randomly selects a secret word from a predefined list of five words. The player must guess the word one letter at a time, with a maximum of six incorrect guesses allowed.

This project demonstrates fundamental Python programming concepts such as variables, strings, lists, sets, loops, conditional statements, functions, and user input validation.

## 🎯 Objectives

- Develop a word-guessing game using Python.
- Understand basic programming logic.
- Practice loops and conditional statements.
- Work with strings, lists, and sets.
- Implement random word selection.
- Handle invalid and repeated user inputs.
- Improve logical thinking and problem-solving skills.

## ✨ Features

- 🎲 Random selection of a secret word.
- 🔤 Guess the word one letter at a time.
- ❤️ Maximum of six incorrect guesses.
- 🔎 Display correctly guessed letters.
- ⌨️ Validate user input.
- 🚫 Prevent repeated letter guesses.
- 🏆 Display a winning message when the word is guessed correctly.
- ❌ Display a game-over message when attempts run out.
- 🔄 Option to play again.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Random Module:** Selects a random word.
- **Strings:** Stores and displays the secret word.
- **Lists:** Stores the predefined words.
- **Sets:** Tracks guessed letters.
- **Loops:** Repeats the guessing process.
- **Conditional Statements:** Checks guesses and game conditions.
- **Functions:** Organizes the code into reusable blocks.
- **Input/Output:** Enables interaction through the terminal.

## 💻 Requirements

- Python 3.x
- Visual Studio Code, PyCharm, IDLE, or another Python editor.
- A terminal or command prompt.

No external libraries are required because the project uses Python's built-in `random` module.

## 📂 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py
└── README.md
```

### File Description

- `hangman.py` — Contains the complete Python source code.
- `README.md` — Contains the project documentation and instructions.

## ⚙️ Installation and Setup

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

Verify the installation by running:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

### Step 2: Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/chatzz06/CodeAlpha_HangmanGame.git
```

### Step 3: Navigate to the Project Folder

```bash
cd CodeAlpha_HangmanGame
```

### Step 4: Run the Program

Run the following command:

```bash
python hangman.py
```

If necessary, on Windows use:

```bash
py hangman.py
```

**Note:** The repository must be created and uploaded to GitHub before the clone command can work.

## 🎮 How to Play

1. Run the Python program.
2. The computer randomly selects a secret word.
3. The word is displayed using underscores.
4. Enter one letter at a time.
5. If the letter is correct, it appears in the word.
6. If the letter is incorrect, one attempt is deducted.
7. Continue guessing until you discover the word or use all six incorrect guesses.
8. Choose whether to play another round.

## 🖥️ Sample Output

```text
========================================
       WELCOME TO HANGMAN GAME
========================================
Guess the hidden word one letter at a time.
You have 6 incorrect guesses allowed.

Word: _ _ _ _ _ _
Incorrect guesses left: 6
Enter a single letter: p
Correct guess!

Word: p _ _ _ _ _
Incorrect guesses left: 6
Enter a single letter: x
Wrong guess!

Word: p _ _ _ _ _
Incorrect guesses left: 5
Enter a single letter: y
Correct guess!
```

**Note:** The actual output may vary depending on the randomly selected word and the letters entered by the player.

## 🧠 Concepts Learned

Through this project, I practiced:

- Python fundamentals.
- Variables and data types.
- Lists, sets, and strings.
- Random word selection.
- `while` and `for` loops.
- `if-else` conditional statements.
- Functions and modular programming.
- User input validation.
- Basic game development logic.
- Problem-solving and debugging.

## 🚀 Future Improvements

Possible enhancements include:

- Adding more words and difficulty levels.
- Displaying Hangman using ASCII art.
- Tracking scores and winning streaks.
- Providing hints to players.
- Loading words from an external file.
- Developing a graphical interface using Tkinter.
- Adding automated tests.

## 🎓 Internship Details

- **Organization:** CodeAlpha
- **Internship Program:** Python Programming Internship
- **Project:** Hangman Game
- **Domain:** Python Programming
- **Repository:** `CodeAlpha_HangmanGame`

## 👨‍💻 Author

**GitHub Username:** chatzz06

**GitHub Profile:** [https://github.com/chatzz06](https://github.com/chatzz06)

**Project Repository:** [https://github.com/chatzz06/CodeAlpha_HangmanGame](https://github.com/chatzz06/CodeAlpha_HangmanGame)

## 📜 License

This project is intended for educational and learning purposes only.

## 🙏 Acknowledgment

I would like to thank **CodeAlpha** for providing the opportunity to improve my Python programming skills through practical internship projects.

---

⭐ If you find this project useful, feel free to star the repository!
