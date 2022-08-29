# Systemctl timers

To use these timers copy the folder systemctl and all it's contents to the
.config folder in your home directory:

```
$ cp -r systemctl ~/.config
```

Now you can enable the timer by issuing:

```
$ systemctl --user enable wallpaper.timer
```

If you change anything in the _wallpaper.timer_ file, like the time for
instance, you will have to reload the daemon:

```
$ systemctl --user daemom-reload
```

Have fun with your automatic wallpaper changes the easy way!
