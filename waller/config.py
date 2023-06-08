import os


class Config:
    walldir = os.path.join('/','data','pictures','walls')
    configpath = os.path.expanduser(os.path.join('~', '.bin', 'wallpaper.cfg'))
    maincat = 'nsfw'
    subcat = 'girls'
    current = ''
    app = 'feh'
    rootpw = 'cyber008'
    random = False
    auto = True
    grub = True
    # sddm = True
    notify = False
