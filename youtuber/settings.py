from collections import namedtuple


TITLE = 'Watch YouTube'
VERSION = '0.0.1'

YT_PLAYLIST_URL = 'https://www.youtube.com/playlist?list='

CREATORS = ['vintagebeef', 'criticalrole']

STREAM = namedtuple('streamer', ['playlist', 'title'])

STREAMS_VINTAGEBEEF = streamer('PLnw9-SvEl3c6D0p4j1P703DEzrwoWNelx', 'From Flames')

                       'PLnw9-SvEl3c6D0p4j1P703DEzrwoWNelx']


STREAMS_CRITICALROLE = ['PL1tiwbzkOjQz7D0l_eLJGAISVtcL7oRu_',
                        'PL1tiwbzkOjQxD0jjAE7PsWoaCrs0EkBH2',
                        'PL1tiwbzkOjQydg3QOkBLG9OYqWJ0dwlxF']
