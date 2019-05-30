import os
import random
from os.path import expanduser
import subprocess
import logging
from threading import Thread
import time


class ChangeWallpaper(Thread):

    # Only for Darwin (MacOS)
    SCRIPT = """/usr/bin/osascript<<END
    tell application "System Events" to tell every desktop to set picture to "%s"
    """
    kill = False
    time = 300  # 5 Minutes

    def __init__(self, order):
        Thread.__init__(self)
        self.order = order

    def get_wallpapers_from_dir(self, dir):
        file_list = os.listdir(dir)
        return file_list

    def set_desktop_background(self, filename):
        subprocess.Popen(self.SCRIPT % filename, shell=True)

    def set_order(self, wallpapers, order):
        display_list = []
        if order == 1:
            # Shuffle
            display_list = wallpapers
        else:
            # Order on the folder
            display_list = wallpapers
            random.shuffle(display_list)

        return display_list

    def run(self):
        print(self.get_time())
        dir = "/Dropbox/AnimeWallpapers"
        home = expanduser("~")
        final_dir = home+""+dir
        wallpapers = self.get_wallpapers_from_dir(final_dir)
        wallpapers = self.set_order(wallpapers, self.order)

        self.kill = False
        status = self.get_kill_status()

        # Helpers | Counters
        c = 0

        while not status and c < len(wallpapers):
            time.sleep(self.get_time())
            status = self.get_kill_status()
            if(status):
                break
            # print(status)
            # print(final_dir+"/"+wallpapers[c])
            self.set_desktop_background(final_dir+"/"+wallpapers[c])
            status = self.get_kill_status()
            c += 1
            if c == len(wallpapers):
                c = 0

    def set_time(self, time_in_seconds):
        self.time = time_in_seconds

    def get_kill_status(self):
        return self.kill

    def get_time(self):
        return self.time

    def get_home(self):
        return str(expanduser("~"))
