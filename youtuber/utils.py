from settings import *

class Utils:
    def __init__(self):
        pass

    def get_playlist_id(self, streamer, title):
        match streamer:
            case 'vintagebeef':
                idx = STREAMS_VINTAGEBEEF[0].index(title)
                return STREAMS_VINTAGEBEEF[idx][1]
            case 'criticalrole':
                idx = STREAMS_CRITICALROLE[0].index(title)
                return STREAMS_CRITICALROLE[idx][1]
