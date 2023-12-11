#!/usr/bin/env python
import os
import sys
import argparse
from datetime import datetime


class Camera:
    def __init__(self, args):
        self.alsa = args.alsa
        self.quiet = args.quiet
        self.filename = args.filename
        self.verbose = args.verbose
        self.framerate = args.framerate
        self.videotype = args.container
        self.prompt = args.prompt
        self.mouse = args.mouse
        # self.app = args.execute

        self.version = "0.1a"

    def header(self):
        os.system('clear')
        t = f"SIMPLE PORN RECORDER {self.version}"
        l = len(t) * "─"
        print(f"{l}\n{t}\n{l}")

    def show_banner(self):
        self.header()
        audio = 'alsa' if self.alsa else 'pulse'
        audio = 'no audio' if self.quiet else audio

        mouse = 'true' if self.mouse else 'false'

        fr = str(self.framerate)
        fn = self.construct_filename()
        ft = self.videotype
        print(f"Output    : {fn}")
        print(f"Video     : {ft}")
        print(f"Audio     : {audio}")
        print(f"Mouse     : {mouse}")
        print(f"Framerate : {fr}")
        print()

    def construct_filename(self):
        now = datetime.now()
        dt_string = now.strftime("%Y%m%d%H%M%S")
        filename = self.filename + "_" + dt_string + "." + self.videotype
        return filename

    def construct(self, fr=29.97):

        # -- create the output filename
        filename = self.construct_filename()

        # -- Construct the sound recorder
        if self.quiet:
            soundrecorder = ""
        else:
            if self.alsa:
                soundrecorder = "-f alsa -ac 2 -i hw:0 "
            else:
                soundrecorder = "-f pulse -ac 2 -i default "

        # -- Construct the full command for ffmpeg
        command = f"ffmpeg -hide_banner -loglevel error -stats "
        command += "-video_size 1920x1080 "
        command += "-f x11grab "
        command += f"-framerate {fr} "

        if not self.mouse:
            command += "-draw_mouse 0 "

        # -- add correct settings per container
        command += "-i :0.0 "
        command += soundrecorder
        command += filename
        return command

    def run(self):
        if self.alsa:
            self.header()
            print("Recording sound from alsa doesn't work on this system.")
            print("Please configure alsa to work correctly.")
            print("Or you could just search for the nearest BBC and suck it!")
            sys.exit()

        if self.quiet and self.alsa:
            self.header()
            print("You can't record audio and be quiet at the same time!")
            sys.exit()

        if self.verbose:
            self.show_banner()

        # -- TODO: Add executing of external program

        command = self.construct(fr=self.framerate)

        if self.prompt:
            # print(command)
            if not self.verbose:
                self.header()
                _ = input("PRESS ENTER TO START RECORDING")
            else:
                _ = input("── PRESS ENTER TO START RECORDING ──")
            print('\033[1A', end='\x1b[2K')
       
        if not self.verbose:
            self.header()
            print("PRESS Q TO STOP RECORDING", end='\n\n')
        else:
            print("── PRESS Q TO STOP RECORDING ──", end="\n\n")
        # -- execute the command
        os.system(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filename',
                        default='recording',
                        help='filename for the recording')

    #parser.add_argument('-x', '--execute',
    #                    default=None,
    #                    help='application to start before recording')

    parser.add_argument('-c', '--container',
                        choices=['mkv', 'mp4'],
                        default='mkv',
                        help='type of video, default mkv')
    
    parser.add_argument('-fr', '--framerate',
                        default=29.97,
                        help='change framerate, default 25')

    parser.add_argument('-p', '--prompt',
                        action='store_true',
                        help='show prompt before start recording')

    parser.add_argument('-m', '--mouse',
                        action='store_true',
                        help='record the mouse cursor')

    parser.add_argument('-a', '--alsa',
                        action='store_true',
                        help='use alsa to record sound, default pulse')
    
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='show more output')

    parser.add_argument('-q', '--quiet',
                        action='store_true',
                        help='do not record sound')
    
    app = Camera(parser.parse_args())
    app.run()
