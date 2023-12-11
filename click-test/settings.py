import os

BACKUPDIR = os.path.join("/", "backups", "sexgames")
DATADIR = os.path.join("/", "data", "downloads", "SexGames")
KEEPDIR = os.path.join(BACKUPDIR, "keep")
CHECKDIR = os.path.join(BACKUPDIR, "checked")

FOLDERS = [ BACKUPDIR, KEEPDIR, CHECKDIR, DATADIR ]
