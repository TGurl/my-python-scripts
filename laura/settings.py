CONFIG = {
         "age": 18,
         "bank": 100,
         "cup": 0,
         "day": 1,
         "energy": 100,
         "rent": 250,
         "sexy": 0,
         "wage": 0,
         "job": None,
         'location': 'home',
         "illegal": False,
         "work_for_tips": False
         }


CUPS = ['a', 'b', 'c', 'd', 'dd', 'ddd', 'e', 'f', 'h', 'k']

# --------------------------------------------------------------------------
# --- Define locations
# --------------------------------------------------------------------------
LOCATIONS = ['home', 'town', 'jobcenter', 'medicalcenter', 'backstreets', 'club']

HOME = ['Town', 'Work', 'Sleep']
TOWN = ['Home', 'Shopping Center', 'Job Center', 'Medical Center', 'Back streets']
MALL = ['town']
JOBCENTER = ['town']
MEDICALCENTER = ['town']
BACKSTREETS= ['town', 'club']
CLUB = ['backstreets']

# --------------------------------------------------------------------------
# --- Define jobs
# --------------------------------------------------------------------------
JOBS = [ "factory", "shop_assistant", "hooker", "escort" ]

FACTORY = { 'name': 'Factory Worker', 'wage': 7, 'illegal': False, 'min_hours': 6, 'max_hours': 8 }
SHOP_ASSISTANT = { 'name': 'Shop Assistant', 'wage': 5, 'illegal': False, 'min_hours': 3, 'max_hours': 10 }
HOOKER = { 'name': 'Hooker', 'wage': None, 'illegal': True, 'min_hours': 4, 'max_hours': 12 }
ESCORT = { 'name': 'Escort', 'wage': None, 'illegal': True, 'min_hours': 4, 'max_hours': 8 }

