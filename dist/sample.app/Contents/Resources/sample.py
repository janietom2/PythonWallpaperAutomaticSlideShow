import rumps
import random
import time
from ChangeWallpaper import ChangeWallpaper


class AwesomeStatusBarApp(rumps.App):

    order = 1
    cw = ChangeWallpaper(order)

    # tl = Tools()

    @rumps.clicked("Start")
    def prefs(self, _):
        self.cw.start()
        rumps.notification("Status", "Process Started",
                           "Wallpaper rotation has Started")

        # rn = random.randint(10, 100)
        # home = self.cw.get_home()
        # rumps.alert(str(home))

    @rumps.clicked("Shuffle")
    def onoff(self, sender):
        sender.state = not sender.state
        self.order = 0

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")


if __name__ == "__main__":
    AwesomeStatusBarApp("", "", "iconwc.png").run()
