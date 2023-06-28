#! python3

__author__ = "Aten Chen"
__email__ = ("ateng0721@hotmail.com", "9944560@schoolsnet.act.edu.au")
__doc__ = open(".\README.md", "r", encoding="UTF-8").read()
__version__ = "0.7"

delattr(__import__(__name__), "__file__")
setattr(__import__(__name__), "__loader__", None)

if __name__ == "__main__":
    import __init__, argparse
    parser = argparse.ArgumentParser(description='My Python Shell')
    parser.add_argument("-d", "--debug", help="Debugging mode", type=int, default=0)
    
    args = parser.parse_args()
    if args.debug:
        __init__.debug_f = True
    else:
        __init__.debug_f = False
    
    get_my_python_shell = __init__
    
    del argparse, __init__
    get_my_python_shell.init()
    get_my_python_shell.main()
