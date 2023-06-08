import os


class Config:
    title = 'Story Teller v0.04'
    storydir = os.path.expanduser(
            os.path.join('~', 'stories'))
    configfile = 'st.cfg'
    lastedited = ''
