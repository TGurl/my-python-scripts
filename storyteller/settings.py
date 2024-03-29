#!/usr/bin/env python
import os

TITLE = "Storyteller"
VERSION = "0.0.4"
STORYDIR = os.path.expanduser(os.path.join("~", "stories"))
CONFIG = os.path.expanduser(
    os.path.join("~", ".local", "share", "storyteller", "st.pickle")
)
LASTOPENED = "promiscuous.md"

DISCLAIMER = [
    "This is a work of fiction, any resemblance to any person living or dead is\n",
    "purely coincidental. All characters are automatically assumed to be of legal\n",
    "age until indicated otherwise. The country where all my stories take place may\n",
    "resemble the United States or Canada, but it's only loosely based upon them.\n",
    "I've taken the liberty of putting a lot of European influences into them.\n",
    "\n",
    "Lastly, I am not a native English speaker, so please forgive any spelling or\n",
    "grammatical mistakes.\n\n",
]
