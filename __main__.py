#! python3

__author__ = "Aten Chen"
__email__ = ("ateng0721@hotmail.com", "9944560@schoolsnet.act.edu.au")
__doc__ = open(".\README.md", "r", encoding="UTF-8").read()
__version__ = "0.7"

if __name__ == "__main__":
    import __init__, argparse
    parser = argparse.ArgumentParser(description='My Python Shell')
    parser.add_argument("-d", "--debug", help="Debugging mode", action='store_true')
    parser.add_argument("-nprtb", "--noprettytb", help="Formatted traceback", action='store_true')
    parser.add_argument("-a", "--ascii", help="Enable ascii charactars", action='store_true')
    parser.add_argument("-ncres", "--nocopyresult", help="Don't copy the result of a expression after evaluating it", action='store_true')

    args = parser.parse_args()

    __init__.debug_f = args.debug
    __init__.pretty_traceback = not args.noprettytb
    __init__.enable_ascii = args.ascii
    __init__.copy_result = not args.nocopyresult
    
    get_my_python_shell = __init__
    
    del argparse, __init__, args, parser

    delattr(__import__(__name__), "__file__")
    setattr(__import__(__name__), "__loader__", None)

    get_my_python_shell.init()
    get_my_python_shell.main()
