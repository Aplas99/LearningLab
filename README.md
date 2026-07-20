# LearnLab

LearnLab is a local, offline learning environment for Python fundamentals, object-oriented programming, and applied mathematics. Its server, lesson checker, assignment setup, and persistence use only Python's standard library.

The curriculum contains 29 focused lessons: 15 Python fundamentals, 6 object-oriented programming lessons, and 8 applied mathematics lessons. Its topic coverage was mapped against the [W3Schools Python tutorial](https://www.w3schools.com/python/), while the explanations, examples, assignments, and tests are original to LearnLab.

Assignments build only on concepts introduced earlier in the sequence. Every assignment includes a suggested approach and a collapsed hint so beginners can get unstuck without immediately seeing a completed answer.

## Start

Python 3.10 or newer is recommended.

```bash
cd /Users/anggelplasencia/Documents/Code-Math
python3 -m learnlab serve
```

Open `http://127.0.0.1:8000` in a browser. Press `Ctrl+C` in the terminal to stop the server.

## Complete an assignment

Each lesson opens its assignment folder in your IDE. Edit `solution.py`, then run the lesson's check command from either that assignment folder or the project root:

```bash
python3 -m learnlab check python/variables
```

A passing check marks the lesson complete. Progress and check history are stored in `data/progress.json`.

### Open assignments in your IDE

Select **Open in IDE** in any assignment, choose an installed editor, and save. LearnLab remembers the choice in `data/settings.json` and opens later assignments with one click. Use **Change IDE** beside the open button whenever you want to switch.

The picker supports Visual Studio Code, Cursor, PyCharm, PyCharm Community, Zed, and Sublime Text. The custom option accepts an executable plus optional arguments, such as `code-insiders --reuse-window`.

Reset from the lesson page or terminal:

```bash
python3 -m learnlab reset python/variables
```

Reset replaces that lesson's `solution.py` with its starter version and clears only that lesson's progress.

## Maintenance

Create any missing assignment workspaces:

```bash
python3 -m learnlab setup
```

Run the application tests:

```bash
python3 -m unittest discover -s tests -v
```
