#! python3

from __init__ import init, Pretty_traceback, user_gbs, config
import sys


sourcefile = " ".join(sys.argv[1:])
config["detail_err"] = True
config["debug_f"] = False
config["no_suggest_code"] = False

try:
    with open(sourcefile, "r", encoding="UTF-8") as file:
        source = file.read()
except (FileNotFoundError, IndexError) as e:
    sys.exit(1)


def main():
    init(run_from_shell=False)
    try:
        exec(compile(source, sourcefile, mode='exec'), user_gbs, user_gbs)
    except Exception as e:
        result = str(Pretty_traceback(e))
        sys.stdout.write(result)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
