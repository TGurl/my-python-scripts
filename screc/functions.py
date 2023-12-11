#!/usr/bin/env python
import os

from config import Config


class Functions:  # pylint: disable=too-few-public-methods
    """Overall functions for screc"""

    def __init__(self):
        pass

    def clear_screen(self):
        """Clear the screen"""
        os.system("clear")

    def myprint(self, message, nl=False):
        """my version of print"""
        newline = "\n\n" if nl else "\n"
        print(message, end=newline)

    def header(self, cls=True, mouse=False):
        """print a simple header"""
        if cls:
            self.clear_screen()
        title = f" {Config.title} - {Config.version} "
        line = len(title) * "-"
        self.myprint(line)
        self.myprint(title)
        self.myprint(line)
        mouse_msg = "Recording mouse cursor" if mouse else "Not recording mouse cursor"
        self.myprint(f"> {mouse_msg}")

    def record_screen(self, filename=None, mouse=False):
        """do the actual recording"""
        recmouse = 1 if mouse else 0

        if filename is None:
            filename = Config.default_filename

        if "." in filename:
            filename = filename.split(".")[0]

        filename = os.path.join(Config.target_dir, filename) + ".mp4"

        print(f"> Recording to {filename}")

        options = "-y -hide_banner -loglevel error -stats "
        options += "-video_size 1920x1080 -thread_queue_size 64 "
        options += f"-framerate 30 -f x11grab -draw_mouse {recmouse} -i :0.0 "
        options += "-f pulse -ac 2 -i default -crf 30 "
        options += "-preset ultrafast -qp 0 -pix_fmt yuv444p"

        cmd = f"ffmpeg {options} {filename}"
        os.system(cmd)
        # print(cmd)
