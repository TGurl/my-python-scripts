#!/usr/bin/env python
# ════════════════════════════════════════════
#  ╔╦╗┬─┐┌─┐┌┐┌┌─┐┌─┐┬┬─┐┬    ╔╦╗┌─┐┌─┐┬  ┌─┐
#   ║ ├┬┘├─┤│││└─┐│ ┬│├┬┘│     ║ │ ││ ││  └─┐
#   ╩ ┴└─┴ ┴┘└┘└─┘└─┘┴┴└─┴─┘   ╩ └─┘└─┘┴─┘└─┘
# ════════════════════════════════════════════

class Config:
    # The first option in the lists are the defaults
    BROWSERS = ["/usr/bin/thorium-browser", "/usr/bin/firefox"]
    TERMINALS = ["/usr/bin/kitty", "/usr/local/bin/st"]

    # Set default applications
    DMENU = "/usr/bin/dmenu"

    # Set the pickles for storing data
    # Don't add the .pickle extension!
    DATADIR = "~/.local/share/tgtools"
    BOOKMARKS = DATADIR + "/bookmarks"

    # Porngame directories
    PGAMEDIRS = ["/lore/sexgames", '/USB/sexgames']
