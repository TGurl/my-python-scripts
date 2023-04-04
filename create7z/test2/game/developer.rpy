# Show filename and line number of current code being executed
# in upper left corner.

# Developer mode.
screen bugTesting_Overlay():
    $ fileLine = renpy.get_filename_line()
    text "[fileLine[0]]:[fileLine[1]]" xpos 10 color "#0f0"
