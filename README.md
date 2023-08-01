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
- ......

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
my_python_shell.bat [-h] [-d] [--noprettytb] [-a] [--nocopyresult] [--nocolor]
```

**Linux**
```
python3 . [-h] [-d] [--noprettytb] [-a] [--nocopyresult] [--nocolor]
```

Usage of the options:
```
  -h, --help      show this help message and exit
  -d, --debug     Debugging mode
  --noprettytb    Formatted traceback
  -a, --ascii     Enable ascii charactars
  --nocopyresult  Don't copy the result of a expression after evaluating it
  --nocolor       No color display
```
#### After starting the shell
1. You should now see the My Python Shell welcome message and the interactive prompt.

2. Enter your Python code at the prompt and press Enter to execute it.

3. View the output of your code and continue entering new code snippets as needed.

4. To exit the shell, you can use the `exit` command or press Ctrl+Z and enter.

## Examples

Here are a few examples to help you get started:

1. **Print hello world!**
![Hello world](/examples/1.png "Hello world!")
-----
2. **Invalid "C-tax"**
![Invalid C-tax](/examples/2.png "Invalid C-tax")
-----
3. **Addition of two numbers**
![Addition of two numbers](/examples/3.png "Addition of two numbers")
-----
4. **Square root of 2**
![Square root of 2](/examples/4.png "Square root of 2")
-----
5. **ZeroDivisionError**
![ZeroDivisionError](/examples/5.png "ZeroDivisionError")
-----
6. **Hello, number!**
![Hello, number](/examples/6.png "Hello, number!")
-----
7. **What's your name?**
![What's your name?](/examples/7.png "What's your name?")

## Extension commands
 ### Commands
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
  - Type `license` to see the license of this shell. (Type `python_license` to see python's license)
 ### Others
  - Type `extend_commands.help_commands()` to see all the commands.
  - Type `extend_commands.help_commands('[your command here]')` for a specific command.
  - Type `win_term.['your cmd here'](['options-1'], ['options-2'], ['options-3'], ...)`. (only on Windows.)

 ### How to register a command
 
 Example:
 ```
In [1]╭→ import math

In [2]╭→

In [3]╭→ @extend_commands
       ├   def calc_sine(*args, **kwargs):
       ├         if not args:
       ├                 num = float(input("Enter a number to calculate: "))
       ├                 print(f"sin({num}) = {math.sin(num)}")
       ├                 return num
       ├         print(f"sin({args[0]}) = {math.sin(args[0])}")
       ├         return args[0]
       ├

In [4]╭→ calc_sine
       ├  Enter a number to calculate: 20
       ├  sin(20.0) = 0.9129452507276277
       ╰  Out[4]: calc_sine(20.0)


In [5]╭→ calc_sine(20.0)
       ├  sin(20.0) = 0.9129452507276277
       ╰  Out[5]: 'calc_sine(20.0)'


In [6]╭→
 ```

 In this case, we defined a command 'calc_sine', which calculates the sine value of a number.
 The command function have two optional prameters: `*args` and `**kwargs`.
 if we type the command function directly, the parameters args will be `[]`, kwargs will be `{}`
 But if we carry a parameter (which is 20) in to the function, the parameter args will be `[20]`.

 ### IMPORTANT ###
 All the extension functions must define two optional parameters: `*args` and `**kwargs`. The function must return `None` or return the input of users.

 
 *We await you to create your own commands and creates a more personal shell!*

## Want to clear your data?
 - Type `clear_data.bat` on Windows.
 - Type `python3 clear_data.py` on Linux

## License

This project is licensed under the [GPL LICENSE](LICENSE)
