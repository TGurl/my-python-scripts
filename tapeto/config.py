import os


class Config:
    title = 'Tapato v0.01'
    current = 'none'
    maincat = 'nsfw'
    subcat = 'girls'
    wpsetter = 'feh'
    rootpw = 'cyber008'
    sddm = True
    grub = True
    auto = True
    random = False
    showwarning = False
    walldir = os.path.join('/',
                           'data',
                           'pictures',
                           'walls')
    grubpath = os.path.join('/',
                            'boot',
                            'grub',
                            'themes',
                            'girls',
                            'background.png')
    sddmpath = os.path.join('/',
                            'usr',
                            'share',
                            'sddm',
                            'themes',
                            'mywall',
                            'Backgrounds',
                            'mywall.png')
