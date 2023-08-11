import os
import pickle
from settings import *


class Engine:
    def __init__(self):
        self.configpath = os.path.expanduser(os.path.join('~', '.local', 'share', 'laura', 'laura.cfg'))
        self.datapath = os.path.expanduser(os.path.join('~', '.local', 'share', 'data'))

    def load_config(self):
        if os.path.exists(self.configpath):
            pickle_in = open(self.configpath, 'rb')
            data = pickle.load(pickle_in)
            pickle_in.close()

            CONFIG['age'] = data['age']
            CONFIG['bank'] = data['bank']
            CONFIG['cup'] = data['cup']
            CONFIG['day'] = data['day']
            CONFIG['energy'] = data['energy']
            CONFIG['rent'] = data['rent']
            CONFIG['sexy'] = data['sexy']
            CONFIG['wage'] = data['wage']
            CONFIG['job'] = data['job']
            CONFIG['illegal'] = data['illegal']
            CONFIG['work_for_tips'] = data['work_for_tips']

    def save_config(self):
        data = {
                'age': CONFIG['age'],
                'bank': CONFIG['bank'],
                'cup': CONFIG['cup'],
                'day': CONFIG['day'],
                'energy': CONFIG['energy'],
                'rent': CONFIG['rent'],
                'sexy': CONFIG['sexy'],
                'wage': CONFIG['wage'],
                'job': CONFIG['job'],
                'illegal': CONFIG['illegal'],
                'work_for_tips': CONFIG['work_for_tips'],
                }
        pickle_out = open(self.configpath, 'wb')
        pickle.dump(data, pickle_out)
        pickle_out.close()
