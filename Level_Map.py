level_map_1 = [
    'X P                        X',  # Row 0
    'XXXXXXXXXXXXXXX       XXXXXX',
    '              X       XX    ',
    '  X  X        X   X   XX     XXXXXXXXXXXXXXXXXXXX',
    '  X      XX           XX   X',
    '  XXXXXXXXXXXXXXXXXXXXXX    ',
    'X                  X       X',
    'X                  X        ',
    'X          XXXXX   X      X ',
    'XXX          X         X    ',
    '     XXX     X    XXXX      ']  # Row 10 (Inclusive)

# Column 0 to Column 27 (Inclusive)

tile_size = 64  # what each x will equal.
screen_width = 1200
screen_height = len(level_map_1) * tile_size  # find the amount of rows which = height so level always fit on screen
