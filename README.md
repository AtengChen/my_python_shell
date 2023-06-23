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

## Getting Started

### Installation

1. Clone the repository or download the source code.

2. Make sure you have Python installed on your system (version 3.9 or higher).

3. Install the required dependencies by running the following command:

pip install -r requirements.txt


### Usage

1. Open a terminal and navigate to the project directory.

2. Run the Python shell by executing the following command:

python my_python_shell.py

3. You should now see the My Python Shell welcome message and the interactive prompt.

4. Enter your Python code at the prompt and press Enter to execute it.

5. View the output of your code and continue entering new code snippets as needed.

6. To exit the shell, you can use the `exit` command or press Ctrl+Z and enter.

## Examples

Here are a few examples to help you get started:

1. Print hello world!
```python
msg = "hello world!"
print(msg) # hello world!
```

2. Addition of two numbers
```python
a = 5
b = 10
result = a + b
print(result) # 15
```

3. Square root of 2
```python
print(modules.math.sqrt(10)) # 3.1622776601683795
```

## Extension commands
 ### commands
  - Type `Exit` to exit.
  - Type `change_theme` to change your theme.
  - Type `clear_data` to clear your user data (All your data).
  - Type `get_time` to view current time.
  - Type `history` to view history. Type `history([history id])` to see the history at history id.
  - Type `load_data` to load a specific user storage file.
  - ...
 - Type `extend_commands.help_commands()` to see all the commands.
 - Type `extend_commands.help_commands('[your command here]')` for a specific command.

## License

This project is licensed under the [GPL LICENSE](https://github.com/AtengChen/my_python_shell/edit/main/LICENSE "GPL LICENSE")
