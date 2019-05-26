import os
import random
from os.path import expanduser
import subprocess
import logging
from threading import Thread
import time


class ChangeWallpaper(Thread):

    # tell application "Finder"
    # set picture rotation to 1 -- turn on wallpaper cycling
    # set change interval to -1 -- force a change to happen right now
    # set desktop picture to POSIX file "%s"
    # set picture rotation to 0  -- turn off wallpaper cycling
    # end tell

    # Only for Darwin (MacOS)
    SCRIPT = """/usr/bin/osascript<<END
    tell application "System Events" to tell every desktop to set picture to "%s"
    END"""

    kill = False

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
            time.sleep(600)
            status = self.get_kill_status()
            if(status):
                break
            print(status)
            print(final_dir+"/"+wallpapers[c])
            self.set_desktop_background(final_dir+"/"+wallpapers[c])
            status = self.get_kill_status()
            c += 1
            if c == len(wallpapers):
                c = 0

    def get_kill_status(self):
        return self.kill
