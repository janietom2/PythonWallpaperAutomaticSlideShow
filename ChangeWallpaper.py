import os
import random
from os.path import expanduser
import subprocess
import logging
from threading import *
import time
from Fetcher import *


class ChangeWallpaper(Thread):

    # Only for Darwin (MacOS)
    SCRIPT = """/usr/bin/osascript<<END
    tell application "System Events" to tell every desktop to set picture to "%s"
    """
    kill = False
    time = 5  # 5 Minutes
    current_wallpaper = ""
    size_batch = 0
    event = None

    def __init__(self, order):
        Thread.__init__(self)
        self.order = order
        self.event = Event()
        self.paused = True
        self.state = Condition()
        # self.event = Thread.Event()

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # Unblock self if waiting.

    def pause(self):
        with self.state:
            self.paused = True  # Block self.

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
            print(display_list)
            random.shuffle(display_list)
            print("now =======")
            random.shuffle(display_list)

        return display_list

    def delete_current_files(self):
        folder = self.get_home()+"/wallpaperslider/wallpapers/tmp"
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    # TODO : Add Category ID (Numerical)
    def get_wallpapers(self):
        info = getJson(
            'https://wallhaven.cc/api/v1/search?categories=010&purity=100&resolutions=1920x1080&sorting=random&order=asc')

        self.size_batch = len(info['data'])

        for x in range(len(info['data'])):
            img_id = info['data'][x]['id']
            img_format = info['data'][x]['file_type']
            img_url = info['data'][x]['path']

            print(img_url)
            path = self.get_home()+"/wallpaperslider/wallpapers/tmp"

            print(path+""+img_id+""+get_format(img_format))

            saveImage(img_url, path, img_id+""+get_format(img_format))

    def create_directory_tmp(self):
        if os.path.isdir(self.get_home()+"/wallpaperslider/wallpapers/tmp"):
            return True
        else:
            path = self.get_home()+"/wallpaperslider/wallpapers/tmp"
            permissions = 0o755
            try:
                os.makedirs(path, permissions)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s" % path)

            return False

    def create_directory_save(self):
        if os.path.isdir(self.get_home()+"/wallpaperslider/wallpapers/saved"):
            return True
        else:
            path = self.get_home()+"/wallpaperslider/wallpapers/saved"
            permissions = 0o755
            try:
                os.mkdir(path, permissions)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s" % path)

            return False

    def go_to_next_wallpaper(self):
        self.event.set()

    def clear_current_event(self):
        self.event.clear()

    def check_set(self):
        return self.event.is_set()

    def run(self):
        self.resume()
        # print(self.event.is_set())
        # print(self.get_time())

        # self.create_directory_tmp()

        # Delete temporal wallpapers
        # self.delete_current_files()

        # Get wallpapers
        # self.get_wallpapers()

        dir = "/wallpaperslider/wallpapers/tmp"
        final_dir = self.get_home()+""+dir
        wallpapers = self.get_wallpapers_from_dir(final_dir)
        wallpapers = self.set_order(wallpapers, self.order)

        self.kill = False
        status = self.get_kill_status()

        # Helpers | Counters
        c = 0

        print("Running")

        while c < len(wallpapers) and not self.event.is_set():
            print("in loop")

            with self.state:
                if self.paused:
                    self.state.wait()

            self.event.wait(self.get_time())
            status = self.get_kill_status()
            if(status):
                self.event.clear()
                continue

            self.set_desktop_background(final_dir+"/"+wallpapers[c])
            status = self.get_kill_status()
            c += 1
            if c == len(wallpapers):
                c = 0
            self.event.clear()

        print("Ending...")
        self.event.clear()

    def set_n_order(self, order):
        self.order = order

    def set_time(self, time_in_seconds):
        self.time = time_in_seconds

    def get_kill_status(self):
        return self.kill

    def get_time(self):
        return self.time

    def get_home(self):
        return str(expanduser("~"))
