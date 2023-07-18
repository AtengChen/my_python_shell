# My Python Shell

Welcome to My Python Shell! This is a Python shell that provides an interactive environment for executing Python code.

## Features

- Runs the code in a sandbox (User namespace) for added security.
- Supports indented code to maintain the Python code's formatting.
- Uses terminal control sequences for a better Terminal User Interface (TUI) appearance.
- Records the history of the inputs for easy access to previous code snippets.
- Displays the latest output on the terminal title for quick reference.
- Utilizes Unicode characters for an enhanced TUI appearance.
- Colors the traceback for improved readability.
- Allows changing the shell's theme to suit personal preferences.
- Can be extended using the extend_commands decorator. Type `extend_commands.help_commands()` to see all available commands.
- ...

## Getting Started

### Installation

1. Clone the repository or download the source code.

2. Make sure you have Python installed on your system (version 3.9 or higher).

3. Install the required dependencies by running the following command:

pip install -r requirements.txt


### Usage

#### Before starting the shell
1. Open a terminal and navigate to the project directory.

2. Run the Python shell by executing the following command format:

**Window**

```
my_python_shell.bat [-h] [-d] [-nprtb] [-a] [-ncres]
```

**Linux**
```
python . [-h] [-d] [-nprtb] [-a] [-ncres]
```

Usage of the options:
```
  -h, --help            show this help message and exit
  -d, --debug           Debugging mode
  -nprtb, --noprettytb  Formatted traceback
  -a, --ascii           Enable ascii charactars
  -ncres, --nocopyresult
                        Don't copy the result of a expression after evaluating it
```
#### After starting the shell
1. You should now see the My Python Shell welcome message and the interactive prompt.

2. Enter your Python code at the prompt and press Enter to execute it.

3. View the output of your code and continue entering new code snippets as needed.

4. To exit the shell, you can use the `exit` command or press Ctrl+Z and enter.

## Examples

Here are a few examples to help you get started:

1. Print hello world!
```
In [1]╭→ msg = "hello world!"

In [2]╭→ print(msg) # hello world!
      ╰  hello world!

In [3]╭→
```

2. Addition of two numbers
```
In [1]╭→ a = 5

In [2]╭→ b = 10

In [3]╭→ result = a + b

In [4]╭→ print(result) # 15
      ╰  15

In [5]╭→
```

3. Square root of 2
```
In [1]╭→ print(modules.math.sqrt(10)) # 3.1622776601683795
      ╰  3.1622776601683795

In [2]╭→
```
4. ZeroDivisionError
```
In [1]╭→ def a():
      ├         def b(n):
      ├                 def c(a, b):
      ├                         return a / b
      ├                 return c(n, n)
      ├         return b(0)
      ├

In [2]╭→ a()
──────────────────────────────────────────────────
Traceback (most recent call last):
  ├  File <shell-2>:1, at module <module>:
  │
  │  → 1│ a()
  │
  ├  File <shell-1>:6, at function a:
  │
  │     1│ def a():
  │     2│      def b(n):
  │     3│              def c(a, b):
  │     4│                      return a / b
  │     5│              return c(n, n)
  │   → 6│     return b(0)
  │     7│
  │     8│
  │
  ├  File <shell-1>:5, at b:
  │
  │     1│ def a():
  │     2│      def b(n):
  │     3│              def c(a, b):
  │     4│                      return a / b
  │   → 5│             return c(n, n)
  │     6│      return b(0)
  │     7│
  │     8│
  │
  ├  File <shell-1>:4, at c:
  │
  │     1│ def a():
  │     2│      def b(n):
  │     3│              def c(a, b):
  │   → 4│                     return a / b
  │     5│              return c(n, n)
  │     6│      return b(0)
  │     7│
  │     8│
  │
  └  ZeroDivisionError: division by zero
──────────────────────────────────────────────────

In [3]╭→
```
5. Hello, number!
```
In [1]╭→ s = ""

In [2]╭→ for i in range(10):
      ├         s += f"Hello, {i}!\n"
      ├

In [3]╭→ s
      ╰  Out[3]:

('Hello, 0!\n'
 'Hello, 1!\n'
 'Hello, 2!\n'
 'Hello, 3!\n'
 'Hello, 4!\n'
 'Hello, 5!\n'
 'Hello, 6!\n'
 'Hello, 7!\n'
 'Hello, 8!\n'
 'Hello, 9!\n')


In [4]╭→ print(s)
      ├  Hello, 0!
      ├  Hello, 1!
      ├  Hello, 2!
      ├  Hello, 3!
      ├  Hello, 4!
      ├  Hello, 5!
      ├  Hello, 6!
      ├  Hello, 7!
      ├  Hello, 8!
      ├  Hello, 9!
      ├

In [5]╭→
```
6. What's your name?
```
In [1]╭→ name = input("What's your name? ")
      ├  What's your name? Aten Chen

In [2]╭→ print(name)
      ├  Aten Chen

In [3]╭→
```

## Extension commands
 ### commands
  - Type `Exit` or `exit` to exit.
  - Type `change_theme` to change your theme.
  - Type `clear_history` to clear all your history.
  - Type `get_time` to view current time.
  - Type `history` to view history. Type `history([history id])` to see the history at history id.
  - Type `load_data` to load a specific user storage file.
  - Type `open_browser` to open a webpage.
  - Type `term` to execute a terminal command (only on non-Windows operating systems). 
  - Type `restart` to restart the shell (Only for debugging options `-d` or `--debug`).
  - Type `tb_history` for the whole traceback history.
  - Type `cls` to clear the screen.
 ### Others
  - Type `extend_commands.help_commands()` to see all the commands.
  - Type `extend_commands.help_commands('[your command here]')` for a specific command.
  - Type `win_term.['your cmd here'](['options-1'], ['options-2'], ['options-3'], ...)` (only on Windows.)

## Want to clear your data?
 - Type `clear_data.bat` on Windows.
 - Type `python3 clear_data.py` on Linux

## License

This project is licensed under the [GPL LICENSE](https://github.com/AtengChen/my_python_shell/edit/main/LICENSE "GPL LICENSE")
