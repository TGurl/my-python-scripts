import os

COMMANDS = [
    ('help', 'show this help'),
    ('create', 'create a new story'),
    ('open', 'open a story'),
    ('delete', 'delete a story'),
    ('list', 'show a list of all stories'),
    ('clear', 'clear the screen'),
    ('exit', 'exit this shell')
]

STORYDIR = os.path.join("/", "data", "www", "stories", "stories")