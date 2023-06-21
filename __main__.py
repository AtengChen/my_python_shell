#! python3

__author__ = "Aten Chen"
__email__ = ("ateng0721@hotmail.com", "9944560@schoolsnet.act.edu.au")
__doc__ = open(".\README.md", "r").read()
__version__ = "0.6"

delattr(__import__(__name__), "__file__")
setattr(__import__(__name__), "__loader__", None)

if __name__ == "__main__":
    __import__("__init__").main()
