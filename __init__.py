"""
A simple and lightweight python shell.
See README.md for more information.
"""


import atexit               # register an atexit func
import ast                  # check the input is executed by eval or exec
import builtins             # modify its functions and get the builtin-function list
import collections          # store the config data
import colorama             # initalize the terminal, needs to install it from pip
import copy                 # copying objects
import ctypes               # Windows console api
import datetime             # only for an extension command
import inspect              # get the module name from a path
import json                 # saving for history
import logging              # log the init process
import os                   # use cmd for controling background colors
import os.path              # path control
import pprint               # pretty display of the displayhook
import pygments             # replace the keywords and builtin-functions with the different colors, needs to install it from pip
import pygments.formatters  #
import pygments.lexers      #
import pyperclip            # copying the result
import re                   # matching file names
import sys                  # 
import termcolor            # color of the terminal, needs to install it from pip
import traceback            # capture the error info and color it
import types                # get NoneType
import unicodedata          # print unicode charactars
import warnings              # 
import webbrowser           # only for an extension command

from utils.command import cmd_list, WINDOWS
from utils.inspect_obj import get_info as _get_info


# set the default vars

exec_flag = None
user_gbs = {}
frame_name = ""
In = []
Out = {}
prompt = ""
code = ""
_exit = sys.exit
_write = sys.stdout.write
_input = builtins.input
_print = builtins.print
exit_f = None
err_pattern = r""
interact_f = None
indent = 0
colors = {"black": [None, None, None, None, None, None, None, None, None, None]}
theme = "black"
banner = ""
logo = ""
user_data = [None, None, None, None, None]
tb_list = []
err_url_dict = {}
config = collections.defaultdict(types.NoneType)
getch = lambda: None
on_error = lambda *args: None
LINE = ""
website = "https://github.com/AtengChen/my_python_shell"

HAS_GOOGLE_SEARCH = None

try:
    import googlesearch
except ImportError:
    HAS_GOOGLE_SEARCH = False
else:
    HAS_GOOGLE_SEARCH = True

LIGHT_VERTICAL_AND_RIGHT        =   "  "
LIGHT_UP_AND_RIGHT              =   "  "
LIGHT_DOWN_AND_RIGHT            =   "  "
LIGHT_HORIZONTAL                =   "  "
LIGHT_VERTICAL                  =   "  "
LIGHT_ARC_DOWN_AND_RIGHT        =   "  "
LIGHT_ARC_UP_AND_RIGHT          =   "  "
RIGHTWARDS_ARROW                =   "  "

try:
    os.mkdir(".shell")
except FileExistsError:
    pass

user_storage_file = os.path.dirname(__file__) + "\\.shell\\user_storage.json"
log_file = os.path.dirname(__file__) + "\\.shell\\init_log.LOG"
error_storage_file = os.path.dirname(__file__) + "\\.shell\\error_urls.json"

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file)
formatter = logging.Formatter('%(relativeCreated)d : %(levelname)s : %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class modules:
    def __call__(self):
        modules = []
        for i in dir(self):
            if not i.startswith("__"):
                modules.append(i)
        return modules


class Extensions_Commands:
    """
    Register a extension command.
    To list all the commands, please call the `help_commands` func
    """

    def __new__(cls, func=None):
        global user_gbs, logger, interact_f
        if func:
            class _c:
                def __repr__(self):
                    res = self.f()
                    if res:
                        return f"{self.f.__name__}({repr(res)})"
                    else:
                        return f"{self.f.__name__}()"
                
                def __call__(self, *args, **kwargs):
                    res = self.f(*args, **kwargs)
                    if res:
                        return f"{self.f.__name__}({repr(res)})"
                    else:
                        return f"{self.f.__name__}()"
                
                def __init__(self):
                    self.f = func
                    self.__doc__ = func.__doc__

            _cls = type(func.__name__, (), {"__repr__": _c.__repr__, "__call__": _c.__call__, "__init__": _c.__init__})
            user_gbs[func.__name__] = _cls()
            setattr(user_gbs["extend_commands"], func.__name__, _cls())
            if not interact_f:
                logger.info(f"Setting extension command {func.__name__} successful")
            
            del _c
            return _cls()
        else:
            sys.stdout.write("Type `extend_commands.help_commands()` to see all the commands.\n")

    @staticmethod
    def help_commands(cmd=None):
        self = user_gbs["extend_commands"]
        if not cmd:
            cmds = ""
            for i in dir(self):
                if hasattr(getattr(self, i), "f"):
                    cmds += f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  {i}\n"

            sys.stdout.write(cmds)
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_UP_AND_RIGHT}  Please type `extend_commands.help_commands('[your command here]')` for a specific command.\n")
        else:
            for i in dir(self):
                attr = getattr(self, i)
                if hasattr(attr, "f"):
                    if i == cmd:
                        doc = attr.__doc__
                        _doc = ""
                        for i in doc.split("\n"):
                            _doc += f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}\t  {i}\n"
                        if _doc:
                            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  Help for command `{cmd}`: \n")
                            sys.stdout.write(f"{_doc}")
                        else:
                            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  No documentation for command `{cmd}`\n")
                        return True
            
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  Couldn't find command `{cmd}`\n")
            return False
    
        
def set_commands():
    global config

    @Extensions_Commands
    def Exit(*args, **kwargs): # although we didn't use it in this code, but we used it in the shell
        """A safe way to exit the shell."""
        global exit_f
        if not args:
            while exit_f:
                answer = ask_yes_no(f"Are you sure you want to exit?")
                if answer == True:
                    exit_f = False
                    sys.stdout.write("Exiting ...\n")
                    save_data()
                    _exit()
                elif answer == False:
                    return answer

        else:
            if args[0] and exit_f:
                exit_f = False
                sys.stdout.write("Exiting ...\n")
                save_data()
                _exit()
            else:
                return args[0]

    @Extensions_Commands
    def history(*args, **kwargs): # usage same as the Exit func
        """
        View the history of the shell. 

        Type `history` for the whole history
        Type `history([history id])` for a specific input 
        """
        global Out, In

        if not args:
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \n{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  History:\n")
            if Out:
                sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \tinput_index\t\tinputs\t\t\toutputs\n")
                for idx, io in Out.items():
                    i, o = io
                    if len(i) > 10:
                        i = i[:10]
                        i += "..."
                        
                    o = o.split("\n")[0]
                    if len(o) > 20:
                        o = o[:20]
                        o += "..."
                    
                    sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \t{idx}\t\t\t{color_code(i)}\t\t\t{o}\n")
                sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \n")
                return
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \tYou don't have any inputs yet! \n{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \n")
            return
        
        sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  History number {args[0]}:\n")
        
        try:
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \t{color_code(Out[str(args[0])][0])}\t{Out[str(args[0])][1]}\n")
        except KeyError:
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \tHistory doesn't exists.\n")
        else:
            return args[0]

    @Extensions_Commands
    def change_theme(*args, **kwargs): # usage same as the history func
        """Change the theme of the shell."""
        global theme, colors
        themes = list(colors)
        theme = themes[(themes.index(theme) + 1) % len(themes)]
        os.system("cls")
    
    @Extensions_Commands
    def open_browser(*args, **kwargs): # usage same as the change_theme func
        """Open a URL in the browser"""
        if not args:
            url = modified_input("Please enter your URL: ")
            webbrowser.open(url)
            return repr(url)

        webbrowser.open(args[0])
        return args[0]
    
    if not WINDOWS:
        @Extensions_Commands
        def term(*args, **kwargs): # usage same as the open_browser func
            """Execute a terminal command."""
            if not args:
                cmd = modified_input("Please enter your command: ")
                res = os.popen(cmd).read()
                if res:
                    for i in res.split("\n"):
                        sys.stdout.write(f"       {LIGHT_VERTICAL_AND_RIGHT}  {i}\n")
                return cmd

            res = os.popen(args[0]).read()

            if res:
                for i in res.split("\n"):
                    sys.stdout.write(f"      {LIGHT_VERTICAL_AND_RIGHT}  {i}\n")

            return args[0]

    @Extensions_Commands
    def clear_history(*args, **kwargs): # usage same as the open_terminal func
        """Clear all the history of the shell."""
        global In, Out, theme, user_gbs
        if not args:
            while True:
                answer = ask_yes_no(f"Are you sure you want to clear all the data?")
                if answer:
                    In = []
                    Out = {}
                    break
                elif answer == False:
                    break
            return answer
        else:
            if args[0]:
                In = []
                Out = {}
            return args[0]

    @Extensions_Commands
    def load_data(*args, **kwargs): # usage same as the clear_data func
        """Load a history file."""
        if repr(clear_history) == "clear_data('Y')":
            load_user_data(modified_input(f"Please enter your storage file's path: "))

    @Extensions_Commands
    def get_time(*args, **kwargs): # usage same as the load_data func
        """Get the current time."""
        sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  Current time: {datetime.datetime.now()}\n")

    @Extensions_Commands
    def cls(*args, **kwargs): # usage same as the get_time func
        """Clear the screen."""
        os.system("cls")

    if config["debug_f"]:
        @Extensions_Commands
        def restart(*args, **kwargs): # usage same as the cls func
            """Restart the shell. It will clear all the data."""
            global user_gbs, user_data, exit_f
            if repr(user_gbs["clear_history"]) == "history('N')":
                return ""
            save_data()
            if not os.system(".\__main__.py"):
                exit_f = False
                _exit()

    @Extensions_Commands
    def tb_history(*args, **kwargs): # usage same as the restart func
        """Get the shell's traceback history."""
        global tb_list
        sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL}  \n")
        if args:
            if args[0] < len(tb_list):
                for line in tb_list[args[0] - 1].split("\n"):
                    sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL}  {line}\n")
            else:
                sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  The requested error index doesn't exists.\n")
            return args[0]

        for tb in range(len(tb_list)):
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  error {tb + 1}: \n")
            for line in tb_list[tb].split("\n"):
                sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL}  \t{line}\n")
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL}  \n")
    
    try:
        user_gbs["python_license"] = builtins.license
    except: 
        user_gbs["python_license"] = None

    @Extensions_Commands
    def license(*args, **kwargs):
        sys.stdout.write(f"\n{LINE}\n")
        if os.system("more LICENSE"):
            sys.stderr.write("\nError reading `LICENSE` file, please check your file have downloaded correctly.")
        sys.stdout.write(f"\n{LINE}\n")

    
def load_user_data(storage_file=user_storage_file):
    global In, Out, theme, user_data, logger, user_storage_file, user_gbs, tb_list, err_url_dict, error_storage_file

    logger.info(f"Loading user storage `{storage_file}`")
    try:
        with open(storage_file, "r") as user_storage, open(error_storage_file, "r") as err_storage:
            user_data = json.load(user_storage)
            In, Out, theme, tb_list = user_data
            err_url_dict = json.load(err_storage)

        logger.info("Loading user storage successful")
    except FileNotFoundError:
        In = []
        Out = {}
        theme = "black"
        tb_list = []
        error_storage_file = {}
        logger.warning("Couldn't find user storage file")
    except Exception as e:
        In = []
        Out = {}
        theme = "black"
        tb_list = []
        err_url_dict = {}
        logger.error(f'Error opening {storage_file}: {e}')
        sys.stderr.write(f"Error ocurred when opening {storage_file}:\n")
        result = modified_traceback(e)
        sys.stdout.write(result)
        sys.stdout.write("\nPlease clear your data\n")
        sys.stdout.flush()
        os.system("pause")


def load_user_modules():
    global user_gbs, logger

    for m, imp in sys.modules.items():
        if not m.startswith("_"):
            logger.info(f"Loading module {m}")
            try:
                setattr(user_gbs["modules"], m, imp)
            except Exception as e:
                logger.error(f"Couldn't load module {m} due to error `{e}`")


def save_data():
    global user_data, In, Out, theme, user_storage_file, tb_list, error_storage_file, err_url_dict
    user_data = (In, Out, theme, tb_list)
    with open(user_storage_file, "w") as f, open(error_storage_file, "w") as f2:
        json.dump(user_data, f)
        json.dump(err_url_dict, f2)


def get_color(idx):
    """
    Get the colors of the current theme.
    """
    global colors, theme
    return (colors[theme][idx], "on_" + theme)


def modified_input(text=""):
    global prompt, _input, _print, indent
    text_list = str(text).split("\n")
    if len(text_list) <= 1:
        return _input(f"{' ' * (len(prompt) - indent)}{LIGHT_VERTICAL_AND_RIGHT}  {text}")
    else:
        for i in text_list[:-1]:
            _print(f"{' ' * (len(prompt) - indent)}{LIGHT_VERTICAL_AND_RIGHT}  {i}")

        return _input(f"{' ' * (len(prompt) - indent)}{LIGHT_VERTICAL_AND_RIGHT}  {text_list[-1]}")


def modified_print(*args, dent=0, stop=True, sep=" ", **kwargs):
    global prompt, _print, indent
    text = sep.join(map(str, args))
    text_list = text.split("\n")
    tab = '\t'
    if len(text_list) <= 1:
        if stop:
            _print(f"{' ' * (len(prompt) - indent)}{LIGHT_ARC_UP_AND_RIGHT}  {tab * dent}{text}", **kwargs)
        else:
            _print(f"{' ' * (len(prompt) - indent)}{LIGHT_VERTICAL_AND_RIGHT}  {tab * dent}{text}", **kwargs)
    else:
        for i in text_list[:-1]:
            _print(f"{' ' * (len(prompt) - indent)}{LIGHT_VERTICAL_AND_RIGHT}  {tab * dent}{i}", **kwargs)

        if stop:
            _print(f"{' ' * (len(prompt) - indent)}{LIGHT_ARC_UP_AND_RIGHT}  {tab * dent}{text_list[-1]}", **kwargs)


def match_filename(name):
    """
    match the name of a file.
    """
    return re.match(r"<shell-(\d+)>", name).groups()[0]


def on_exit():
    """
    Ask user to exit
    """
    global exit_f
    exit_f = True
    try:
        return repr(builtins.exit)
    except Exception as e:
        sys.stderr.write("My Python Shell Internal Error: \n" + modified_traceback(e))
        exit_f = False
        exit(1)


def color_website(url):
    return termcolor.colored(url, *get_color(10), ['underline'])


def ask_yes_no(question, options=["y", "n"]):
    global prompt, indent, getch

    if len(options) != 2:
        raise ValueError("Options length must be two.")

    if WINDOWS:
        import msvcrt
        getch = msvcrt.getch
        del msvcrt
    else:
        import termios, tty

        def getch():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

        del termios, tty

    sys.stdout.write(f"{' ' * (len(prompt) - indent)}{LIGHT_VERTICAL_AND_RIGHT}  {question} [{options[0]}/{options[1]}]")
    sys.stdout.flush()
    answer = getch().decode("latin").lower()
    sys.stdout.write("\n")

    if answer in options:
        if answer == "y":
            return True
        else:
            return False
    else:
        return None
        

def modified_displayhook(obj):
    """
    The modified version of sys.displayhook
    """
    global Out, In, user_gbs, config

    try:
        if obj is not None:
            copy_cache = False

            if (obj == user_gbs["_"]) and (type(obj).__module__ == "builtins"):
                try:
                    eval(repr(obj))
                except SyntaxError:
                    pass
                else:
                    try:
                        repr_obj = Out[str(len(Out))][1]
                        copy_cache = True
                    except KeyError:
                        copy_cache = False

            if not copy_cache:
                repr_obj = pprint.pformat(obj, indent=4) if hasattr(obj, "__iter__") else repr(obj)
                
            Out[len(In)] = (In[-1], repr_obj)
            user_gbs["_"] = obj
            if "\n" in repr_obj:
                sys.stdout.write(f"{' ' * (len(prompt) - indent)}{LIGHT_ARC_UP_AND_RIGHT}  " + termcolor.colored(f"Out[{len(In)}]", *get_color(0)) + f": \n\n{repr_obj}\n")
            else:
                sys.stdout.write(f"{' ' * (len(prompt) - indent)}{LIGHT_ARC_UP_AND_RIGHT}  " + termcolor.colored(f"Out[{len(In)}]", *get_color(0)) + f": {repr_obj}\n")
            
            sys.stdout.write(f"\x1b]0;My python shell - {repr_obj}\x07\r\n")
            if config["copy_result"]:
                pyperclip.copy(repr_obj)
            sys.stdout.write(LINE + "\n")

    except (IndexError, AttributeError): # if encounters a bug
        sys.__displayhook__(obj)


def modified_traceback(exc, show_detail=False):
    """
    A modified version of python's traceback
    """
    global code, In, user_gbs, config, website, err_url_dict
    
    traceback_list = traceback.extract_tb(exc.__traceback__)
    result = ""
    tb_main = ""
    err_count = 0
    is_syntaxerror = isinstance(exc, SyntaxError)

    for tb in traceback_list:
        filename, line_num, func_name, error_code = tb
        err_count += 1

        if is_syntaxerror and (err_count == len(traceback_list)):
            filename = f"<shell-{len(In)}>"
            line_num = exc.lineno
            func_name = "<module>"
            error_code = In[-1]

        hide_detail = ((filename in __file__) and (not config["debug_f"])) and (not show_detail)
        if hide_detail:
            continue

        err_func_type = ""
        if func_name == "<module>":
            try:
                match_filename(filename)
            except AttributeError:
                pass
            else:
                error_code = code
                err_func_type = "module"
            display_filename = f"Shell {termcolor.colored(filename, *get_color(4))}"
        else:
            if func_name in user_gbs:
                err_func_type = type(user_gbs[func_name]).__name__
            else:
                err_func_type = "\b"
            module_name = inspect.getmodulename(filename)
            if module_name:
                display_filename = f"Module {termcolor.colored(module_name, *get_color(4))}"
            else:
                try:
                    match_filename(filename)
                except AttributeError:
                    display_filename = f"File {termcolor.colored(filename, *get_color(4))}"
                else:
                    display_filename = f"Shell {termcolor.colored(filename, *get_color(4))}"

        if (err_count > 4) and isinstance(exc, RecursionError):
            tb_main += f"  {LIGHT_VERTICAL_AND_RIGHT}  ...\n"
            break
        
        display_code = ""
        try:
            error_input = In[int(match_filename(filename)) - 1].split("\n")
            error_code = error_input[line_num - 1]

            for line_index in range(len(error_input)):
                if not (line_index == line_num - 1):
                    display_line_number = str(line_index + 1)
                    display_line_number = display_line_number.rjust(len(str(len(error_input) + 1)) - len(display_line_number) + 1)
                    display_code += f"  {LIGHT_VERTICAL}\t{termcolor.colored(display_line_number, *get_color(3))}{LIGHT_VERTICAL} {color_code(error_input[line_index])}\n"
                else:
                    display_line_number = RIGHTWARDS_ARROW + ' ' + str(line_num)
                    display_line_number = display_line_number.rjust(len(str(len(error_input) + 1)) - len(display_line_number) + 5)
                    
                    if is_syntaxerror and (err_count == len(traceback_list)):
                        c = error_code.replace(error_code.strip(), color_code(error_code, exc.offset))
                        display_code += f"  {LIGHT_VERTICAL}  {termcolor.colored(display_line_number, *get_color(1))}{LIGHT_VERTICAL} {c}\n"
                    else:
                        display_code += f"  {LIGHT_VERTICAL}  {termcolor.colored(display_line_number, *get_color(1))}{LIGHT_VERTICAL} {color_code(error_code)}\n"
        except (IndexError, AttributeError):
            if hide_detail:
                display_code += f"  {LIGHT_VERTICAL}  {termcolor.colored('0', *get_color(1))}{LIGHT_VERTICAL} {termcolor.colored('(Cannot find original code)', *get_color(7))}\n"
            else:
                display_line_number = RIGHTWARDS_ARROW + ' ' + str(line_num)
                display_code += f"  {LIGHT_VERTICAL}  {termcolor.colored(display_line_number, *get_color(1))}{LIGHT_VERTICAL} {color_code(error_code)}\n"
        
        tb_main += f"  {LIGHT_VERTICAL_AND_RIGHT}  {display_filename}" \
                       f":{termcolor.colored(line_num, *get_color(5))}, " \
                       f"at {termcolor.colored(err_func_type, *get_color(9))} {termcolor.colored(func_name, *get_color(6))}: \n" \
                       f"  {LIGHT_VERTICAL}\n{display_code}  {LIGHT_VERTICAL}\n"

    if tb_main:
        if is_syntaxerror:
            err_msg = f"{type(exc).__name__}: Invalid Syntax"
        else:
            err_msg = f"{type(exc).__name__}: {exc}"
        result += f"{LINE}\nTraceback (most recent call last):\n{tb_main}  {LIGHT_UP_AND_RIGHT}  {termcolor.colored(err_msg, *get_color(7))}\n\n"
        if config["detail_err"] and (not show_detail):
            if err_msg in err_url_dict:
                url = err_url_dict[err_msg]
            else:
                url = googlesearch.lucky(err_msg)
                err_url_dict[err_msg] = url

            result += f"\nFor more imformation about this error, please look at: \n\t{color_website(url)}\n\n{LINE}\n\n"
    else:
        err_cause = f": {exc}" if str(exc) else ""
        result += termcolor.colored(f"\nInternal Error: {type(exc).__name__}{err_cause}\n\n", *get_color(7)) + modified_traceback(exc, show_detail=True) + "\n" + LINE + "\n"
    return result


def parse_code(inp_code):
    """
    Parse the code
    """
    global frame_name, user_gbs, Out
    
    mod = ast.parse(inp_code, filename=frame_name)

    if len(mod.body) == 0:
        return

    if isinstance(mod.body[-1], ast.Expr):
        expr = ast.Expression(mod.body[-1].value)
        del mod.body[-1]
    else:
        expr = None
    
    if len(mod.body):
        exec(compile(mod, frame_name, mode='exec'), user_gbs, user_gbs)
        Out[len(In)] = (inp_code, "")
        return

    if expr is not None:
        modified_displayhook(eval(compile(expr, frame_name, mode='eval'), user_gbs, user_gbs))


def code_is_complete(inp_code):
    try:
        ast.parse(inp_code, mode='exec')
        return True
    except SyntaxError:
        return False


def input_code(pmt=None):
    global In, exec_flag, frame_name, prompt, exit_f, _input
    try:
        if not pmt:
            prompt = pmt = termcolor.colored(f"\nIn [{len(In) + 1}]", *get_color(3))
        sys.ps1 = f"{pmt}{LIGHT_ARC_DOWN_AND_RIGHT}{RIGHTWARDS_ARROW} "
        inp_code = _input(sys.ps1)

    except EOFError:
        In.append(on_exit())
        inp_code = In[-1]

    except RuntimeError:
        exit_f = False
        _exit()

    if not code_is_complete(inp_code):
        if not exec_flag:
            block = ""
            exec_flag = False
            while True:
                if not exec_flag:
                    try:
                        sys.ps2 = f"{' ' * (len(prompt) - indent)}{LIGHT_VERTICAL_AND_RIGHT}   "
                        line = _input(sys.ps2)
                    except EOFError:
                        raise IndentationError("expected an indented block")
                    except RuntimeError:
                        exit_f = False
                        _exit()
                    block += line + "\n"
                else:
                    exec_flag = False
                    break
                if not line.strip():
                    exec_flag = True
                    continue
            inp_code += "\n" + block
        else:
            exc = SyntaxError("invalid syntax")
            exc.lineno = 1
            raise exc

    In.append(inp_code)
    frame_name = f"<shell-{len(In)}>"
    return inp_code


def color_code(code_string, offset=None):
    """
    colors the code.
    """
    if not config["nocolor"]:
        if offset:
            code_string = code_string.strip()
            left = code_string[:offset - 1]
            char = code_string[offset - 1]
            right = code_string[offset:]
            result = f"{left}{termcolor.colored(char, 'white', 'on_yellow')}{right}"
        else:
            result = pygments.highlight(code_string, pygments.lexers.PythonLexer(), pygments.formatters.TerminalFormatter(bg="dark")).split("\n")[0]
    
    result = result.replace("\t", f"\b{termcolor.colored(LIGHT_VERTICAL, attrs=['dark'])}\t")

    return result


def modified_write(string, color=colors[theme][8], on_color=theme, **kwargs):
    global _write, exit_f
    if exit_f:
        _write(termcolor.colored(string, color, "on_" + on_color), **kwargs)


def get_info(obj):
    info_data = _get_info(obj)

    for k, v in info_data.items():
        if k == "document":
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  document: \n")
            modified_print(v, dent=1, stop=False)
        elif k == "attributes":
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  attributes: \n")
            for i in v:
                sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  \t{color_code(i)}\n")
        elif (k == "name") or (k == "type"):
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  {k}:\t\t{color_code(v)}\n")
        else:
            sys.stdout.write(f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}  {k}:\t\t{v}\n")

            
def init(write_banner=True):
    """
    Initalize the whole shell:
        Set up the environment vars
        Initalize the console
        Modify builtin-funcs, including builtins and sys
        Write the banner
        ...

    """
    global exec_flag, \
           user_gbs, \
           frame_name, \
           In, \
           Out, \
           _exit, \
           exit_f, \
           prompt, \
           interact_f, \
           on_error, \
           colors, \
           theme, \
           banner, \
           LINE, \
           user_data, \
           logger, \
           logo, \
           config, \
           indent, \
           \
           LIGHT_VERTICAL_AND_RIGHT, \
           LIGHT_UP_AND_RIGHT, \
           LIGHT_DOWN_AND_RIGHT, \
           LIGHT_HORIZONTAL, \
           LIGHT_VERTICAL, \
           LIGHT_ARC_DOWN_AND_RIGHT, \
           LIGHT_ARC_UP_AND_RIGHT, \
           RIGHTWARDS_ARROW

    
    if config["debug_f"]:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.CRITICAL)

    run_from_console = False
    if sys.platform == "win32":
        kernel32 = ctypes.windll.kernel32
        console = kernel32.GetConsoleWindow()
        if console or os.getenv('PROMPT'):
            run_from_console = True
    else:
        if sys.__stdin__:
            run_from_console = True

    if not run_from_console:
        if not config["debug_f"]:
            sys.stderr.write("\nCouldn't detect console window, you need to run this program in a terminal.\n")
            sys.exit()

    logger.info(f"This is my_python_shell on {sys.platform} terminal")
    logger.info(f"Current time: {datetime.datetime.now()}")
    logger.info("Initializing terminal")
    colorama.init()
    logger.info("Initializing terminal complete")
    
    # set the charactars
    if not config["enable_ascii"]:
        LIGHT_VERTICAL_AND_RIGHT        =   unicodedata.lookup("BOX DRAWINGS LIGHT VERTICAL AND RIGHT") # U+251C
        LIGHT_UP_AND_RIGHT              =   unicodedata.lookup("BOX DRAWINGS LIGHT UP AND RIGHT")       # U+2514
        LIGHT_DOWN_AND_RIGHT            =   unicodedata.lookup("BOX DRAWINGS LIGHT DOWN AND RIGHT")     # U+250C
        LIGHT_HORIZONTAL                =   unicodedata.lookup("BOX DRAWINGS LIGHT HORIZONTAL")         # U+2500
        LIGHT_VERTICAL                  =   unicodedata.lookup("BOX DRAWINGS LIGHT VERTICAL")           # U+2502
        LIGHT_ARC_DOWN_AND_RIGHT        =   unicodedata.lookup("BOX DRAWINGS LIGHT ARC DOWN AND RIGHT") # U+256D
        LIGHT_ARC_UP_AND_RIGHT          =   unicodedata.lookup("BOX DRAWINGS LIGHT ARC UP AND RIGHT")   # U+2570
        RIGHTWARDS_ARROW                =   unicodedata.lookup("RIGHTWARDS ARROW")                      # U+2192
    else:
        LIGHT_VERTICAL_AND_RIGHT        =   r"|-"
        LIGHT_UP_AND_RIGHT              =   r"\-"
        LIGHT_DOWN_AND_RIGHT            =   r"/-"
        LIGHT_HORIZONTAL                =   r"--"
        LIGHT_VERTICAL                  =   r"| "
        LIGHT_ARC_DOWN_AND_RIGHT        =   r"r-"
        LIGHT_ARC_UP_AND_RIGHT          =   r"+-"
        RIGHTWARDS_ARROW                =   r"->"

    LINE = (os.get_terminal_size().columns - 2) * LIGHT_HORIZONTAL

    load_user_data()
    user_gbs = {"__name__": "__main__",
                "__doc__": banner,
                "__package__": None,
                "__spec__": None,
                "__annotations__": {},
                "__loader__": None,
                "In": In,
                "Out": Out,
                "__dict__": user_gbs,
                "_": In[-1] if In else "",
                "extend_commands": Extensions_Commands,
                "modules": modules,
                "quick_help": get_info,
                "get_info": get_info, 
                "ask_yes_no": ask_yes_no,
                "config": config}

    load_user_modules()
    user_gbs["modules"] = user_gbs["modules"]()

    if WINDOWS:
        class terminal_commands:
            __doc__ = os.popen("help").read()
                        
            def __getattr__(self, name):
                if name.upper() not in cmd_list:
                    return
                
                class _c:
                    def __call__(self, *options, cmd=name):
                        modified_print(os.popen(cmd + " " + " ".join(options)).read())
                    
                    def __repr__(self, cmd=name):
                        return os.popen(f"help {cmd}").read()
                
                return type(name, (), {"__call__": _c.__call__, "__repr__": _c.__repr__})()

        user_gbs["win_term"] = terminal_commands()

    interact_f = False
    exec_flag = False
    exit_f = True
    frame_name = f"<shell-{len(In)}>"

    if not config["nocolor"]:
        indent = 15
        colors = {"black": ["light_red", "light_yellow", "light_magenta", "light_green", "magenta", "yellow", "light_cyan", "red", "white", "blue", "light_blue"],
              "white": ["light_green", "light_blue", "light_green", "light_magenta", "green", "blue", "red", "green", "black", "yellow", "light_yellow"]}
    else:
        indent = 10
    sys.stdout.write = modified_write
    
    logger.info("Setting theme successful")

    sys.stdout.write(f"\x1b]0;My python shell\x07\r")

    _exit = sys.exit

    set_commands()

    builtins.exit = user_gbs["Exit"]
    builtins.quit = user_gbs["Exit"]
    builtins.input = modified_input
    builtins.print = modified_print

    def on_exit():
        return repr(user_gbs["Exit"])
    
    def _on_error(*args):
        global exit_f
        os.system("PAUSE")
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        sys.stderr = sys.__stderr__
        sys.displayhook = sys.__displayhook__
        sys.excepthook = sys.__excepthook__
        sys.stderr.write(f"Internal Error: \n\n{modified_traceback(args[1], show_detail=True)}\n"
                         f"If you suspect this is a My_Python_Shell issue, please report it at: {color_website(website)}\n\n"
                         f"{LINE}\n\n")
        init(write_banner=False)
        main()
    
    atexit.register(on_exit)
    logger.info("Registering exit-func successful")

    sys.displayhook = modified_displayhook

    on_error = _on_error

    sys.excepthook = copy.copy(on_error)

    prompt = termcolor.colored(f"\nIn [0]", *get_color(3))
    sys.ps1 = f"{prompt}{LIGHT_ARC_DOWN_AND_RIGHT}{RIGHTWARDS_ARROW} "
    sys.ps2 = f"{(len(prompt) - indent) * ' '}{LIGHT_VERTICAL_AND_RIGHT}   "
    logger.info("Setting prompt successful")
    
    logo = r"""
  __  __         _____       _   _                    _____ _          _ _
 |  \/  |       |  __ \     | | | |                  / ____| |        | | |
 | \  / |_   _  | |__) |   _| |_| |__   ___  _ __   | (___ | |__   ___| | |
 | |\/| | | | | |  ___/ | | | __|  _ \ / _ \|  _ \   \___ \|  _ \ / _ \ | |
 | |  | | |_| | | |   | |_| | |_| | | | (_) | | | |  ____) | | | |  __/ | |
 |_|  |_|\___ | |_|    \___ |\__|_| |_|\___/|_| |_| |_____/|_| |_|\___|_|_|
          __/ |         __/ |                                 For beginners
         |___/         |___/             A simple shell that was easy to use
    """

    banner = f"\n{termcolor.colored(logo, *get_color(6))}\n\n{LINE}\n\n " \
             f"Features:\n" \
             f"    {LIGHT_DOWN_AND_RIGHT}{LIGHT_HORIZONTAL}  Runs the code in a sandbox (User namespace)\n" \
             f"    {LIGHT_VERTICAL_AND_RIGHT}{LIGHT_HORIZONTAL}  Supports indented code\n" \
             f"    {LIGHT_VERTICAL_AND_RIGHT}{LIGHT_HORIZONTAL}  Uses the terminal control sequences for better TUI appearance\n" \
             f"    {LIGHT_VERTICAL_AND_RIGHT}{LIGHT_HORIZONTAL}  Record the history of the inputs\n" \
             f"    {LIGHT_VERTICAL_AND_RIGHT}{LIGHT_HORIZONTAL}  Show the latest output on the title of the terminal\n" \
             f"    {LIGHT_VERTICAL_AND_RIGHT}{LIGHT_HORIZONTAL}  Uses Unicode characters for better TUI appearance\n" \
             f"    {LIGHT_VERTICAL_AND_RIGHT}{LIGHT_HORIZONTAL}  Coloring the traceback\n" \
             f"    {LIGHT_VERTICAL_AND_RIGHT}{LIGHT_HORIZONTAL}  Change the theme\n" \
             f"    {LIGHT_UP_AND_RIGHT}{LIGHT_HORIZONTAL}  Can extend using the extend_commands decorator. (Type `extend_commands.help_commands()` to see all the commands.)\n\n{LINE}\n\n" \
             f"\t\t\t\tHappy Using!\n\n\n"

    logger.info("Initializing shell successful.")
    
    if write_banner:
        sys.stdout.write(banner)


def main():
    """
    Main part of the shell
    """
    global exec_flag, user_gbs, frame_name, prompt, err_pattern, interact_f, code, exit_f, tb_list, pretty_traceback, _exit, on_error
    interact_f = True

    try:
        while True:
            try:
                code = input_code()
                parse_code(code)
                save_data()
            except SystemExit:
                if exit_f:
                    warnings.warn('To exit, please use EOF, exit or quit.')
                else:
                    _exit()
            except RuntimeError as e:
                on_error(None, e, None)
            except Exception as e:
                Out[len(In)] = (code, termcolor.colored(e, *get_color(7)))
                if config["pretty_traceback"] or config["pretty_traceback"] == None:
                    result = modified_traceback(e)
                elif config["pretty_traceback"] == False:
                    result = traceback.format_exc()
                sys.stdout.write(result)
                tb_list.append(result)
            else:
                user_gbs["__dict__"] = user_gbs

    except KeyboardInterrupt as e:
        sys.stderr.write(termcolor.colored(f"\nKeyboardInterrupt\n", *get_color(7)))
        main()
    return 0


if not (__name__ == "__main__"):
    __all__ = ["main", "init", "Extensions_Commands", "config"]
else:
    sys.stderr.write("Please run this script by __main__.py\n")
    sys.stderr.flush()
    os.system("PAUSE")
    
    if os.system("python " + os.path.dirname(__file__)):
        raise Exception("`__main__.py` not found")
