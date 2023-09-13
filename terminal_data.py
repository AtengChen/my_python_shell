import unicodedata


def get_char_data(ascii=False):
    if not ascii:
        LIGHT_VERTICAL_AND_RIGHT        =   unicodedata.lookup("BOX DRAWINGS LIGHT VERTICAL AND RIGHT") # U+251C
        LIGHT_UP_AND_RIGHT              =   unicodedata.lookup("BOX DRAWINGS LIGHT UP AND RIGHT")       # U+2514
        LIGHT_DOWN_AND_RIGHT            =   unicodedata.lookup("BOX DRAWINGS LIGHT DOWN AND RIGHT")     # U+250C
        LIGHT_HORIZONTAL                =   unicodedata.lookup("BOX DRAWINGS LIGHT HORIZONTAL")         # U+2500
        LIGHT_VERTICAL                  =   unicodedata.lookup("BOX DRAWINGS LIGHT VERTICAL")           # U+2502
        LIGHT_ARC_DOWN_AND_RIGHT        =   unicodedata.lookup("BOX DRAWINGS LIGHT ARC DOWN AND RIGHT") # U+256D
        LIGHT_ARC_UP_AND_RIGHT          =   unicodedata.lookup("BOX DRAWINGS LIGHT ARC UP AND RIGHT")   # U+2570
        RIGHTWARDS_ARROW                =   unicodedata.lookup("RIGHTWARDS ARROW")                      # U+2192
        BLACK_UPPER_LEFT_TRIANGLE       =   unicodedata.lookup("BLACK UPPER LEFT TRIANGLE")             # U+25E4
    else:
        LIGHT_VERTICAL_AND_RIGHT        =   r"|-"
        LIGHT_UP_AND_RIGHT              =   r"\-"
        LIGHT_DOWN_AND_RIGHT            =   r"/-"
        LIGHT_HORIZONTAL                =   r"--"
        LIGHT_VERTICAL                  =   r"| "
        LIGHT_ARC_DOWN_AND_RIGHT        =   r"r-"
        LIGHT_ARC_UP_AND_RIGHT          =   r"+-"
        RIGHTWARDS_ARROW                =   r"->"
        BLACK_UPPER_LEFT_TRIANGLE       =   r"|>"

    return LIGHT_VERTICAL_AND_RIGHT, \
           LIGHT_UP_AND_RIGHT, \
           LIGHT_DOWN_AND_RIGHT, \
           LIGHT_HORIZONTAL, \
           LIGHT_VERTICAL, \
           LIGHT_ARC_DOWN_AND_RIGHT, \
           LIGHT_ARC_UP_AND_RIGHT, \
           RIGHTWARDS_ARROW, \
           BLACK_UPPER_LEFT_TRIANGLE


colors = {"black": ["light_red", "light_yellow", "light_magenta", "light_green", "magenta", "yellow", "light_cyan", "red", "white", "blue", "light_blue"],
      "white": ["light_green", "light_blue", "light_green", "light_magenta", "green", "blue", "red", "green", "black", "yellow", "light_yellow"]}
