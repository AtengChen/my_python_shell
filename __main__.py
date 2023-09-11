#! python3

import os.path

__author__ = "Aten Chen"
__email__ = ("ateng0721@hotmail.com", "9944560@schoolsnet.act.edu.au")
__doc__ = open(os.path.dirname(__file__) + "\\README.md", "r", encoding="UTF-8").read()
__version__ = "0.9"

if __name__ == "__main__":
    import argparse, sys, __init__

    get_my_python_shell = __init__

    parser = argparse.ArgumentParser(description='My Python Shell')
    parser.add_argument("-d", "--debug", help="Debugging mode", action='store_true')
    parser.add_argument("--noprettytb", help="Formatted traceback", action='store_true')
    parser.add_argument("-a", "--ascii", help="Enable ascii charactars", action='store_true')
    parser.add_argument("--nocopyresult", help="Don't copy the result of a expression after evaluating it", action='store_true')
    parser.add_argument("--nocolor", help="No color display", action='store_true')
    parser.add_argument("--nodetailerr", help="No detailed error", action='store_true')
    parser.add_argument("--nohistory", help="Don't save history", action='store_true')
    parser.add_argument("-u", "--user_profile", help="The path to user data. Default path `./.shell`.")
    parser.add_argument("--nosuggest", help="Don't suggest complete code when an error happens.", action='store_true')
    

    args = parser.parse_args()

    __init__.config["debug_f"] = args.debug
    __init__.config["pretty_traceback"] = not args.noprettytb
    __init__.config["enable_ascii"] = args.ascii
    __init__.config["copy_result"] = not args.nocopyresult
    __init__.config["nocolor"] = args.nocolor
    __init__.config["detail_err"] = not args.nodetailerr
    __init__.config["nohistory"] = args.nohistory
    __init__.config["user_profile"] = args.user_profile
    __init__.config["no_suggest_code"] = args.nosuggest
    
    del argparse, __init__, args, parser

    delattr(__import__(__name__), "__file__")
    setattr(__import__(__name__), "__loader__", None)
    setattr(__import__(__name__), "__spec__", None)
    
    get_my_python_shell.init()
    sys.exit(get_my_python_shell.main())
