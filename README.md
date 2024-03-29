# My Python Shell

Welcome to My Python Shell! This is a Python shell that provides an interactive environment for executing Python code.

## Features

- [x] Supports indented code to maintain the Python code's formatting.
- [x] Uses terminal control sequences for a better Terminal User Interface (TUI) appearance.
- [x] Records the history of the inputs for easy access to previous code snippets.
- [x] Displays the latest output on the terminal title for quick reference.
- [x] Utilizes Unicode characters for an enhanced TUI appearance.
- [x] Colors the traceback for improved readability.
- [x] Give traceback tips
- [x] Allows changing the shell's theme to suit personal preferences.
- [x] Can be extended using the extend_commands decorator. Type `extend_commands.help_commands()` to see all available commands.
- [x] ......

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
my_python_shell.bat [-h] [-d] [--noprettytb] [-a] [--nocopyresult] [--nocolor] [--nodetailerr] [--nohistory] [-u USER_PROFILE] [--nosuggest]
```

**Linux**
```
python3 . [-h] [-d] [--noprettytb] [-a] [--nocopyresult] [--nocolor] [--nodetailerr] [--nohistory] [-u USER_PROFILE] [--nosuggest]
```

Usage of the options:
| argument | description |
| ----------- | ----------- |
| `-h` or `--help` | Show this help message and exit |
| `-d` or `--debug` | Turn on debugging mode |
| `--noprettytb` | no formatted traceback |
| `-a` or `--ascii` | Enable ascii charactars |
| `--nocopyresult` | Don't copy the result of a expression after evaluating it |
| `--nocolor` | No color display |
| `--nodetailerr` | No detailed error |
| `--nohistory` | Don't save history |
| `-u USER_PROFILE` or `--user_profile USER_PROFILE` | The path to user data. Default path `./.shell`. |
| `--nosuggest` | Don't suggest complete code when an error happens. |


#### After starting the shell
1. You should now see the My Python Shell welcome message and the interactive prompt.

2. Enter your Python code at the prompt and press Enter to execute it.

3. View the output of your code and continue entering new code snippets as needed.

4. To exit the shell, you can use the `exit` command or press Ctrl+Z and enter.

## Examples

Here are a few examples to help you get started:
 
Print hello world!
===============
![Hello world](/examples/1.png "Hello world!")
-----
**Invalid "C-tax"**
===============
![Invalid C-tax](/examples/2.png "Invalid C-tax")
-----
**Addition of two numbers**
===============
![Addition of two numbers](/examples/3.png "Addition of two numbers")
-----
**Square root of 2**
===============
![Square root of 2](/examples/4.png "Square root of 2")
-----
**ZeroDivisionError**
===============
![ZeroDivisionError](/examples/5.png "ZeroDivisionError")
-----
**Hello, number!**
===============
![Hello, number](/examples/6.png "Hello, number!")
-----
**What's your name?**
===============
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
 ### Builtin tools
  - Type `extend_commands.help_commands()` to see all the commands.
  - Type `extend_commands.help_commands('[your command here]')` for a specific command.
  - Type `win_term.['your cmd here'](['options-1'], ['options-2'], ['options-3'], ...)`. (only on Windows.)
  - Type `modules.['your builtin module here']` to get the module you want.
  - Type `quick_help.('[your object]')` or `get_info.('[your object]')` to get a quick help for a object.

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
