import rumps
import time
from ChangeWallpaper import ChangeWallpaper


class AwesomeStatusBarApp(rumps.App):

    cw = None
    order = 1

    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__(
            "Wallpaper Change", "", "trayicon.png")
        self.menu = ["Start", "Shuffle", "Stop",
                     "About", ['Time', ['10 Seconds', '30 Seconds', '1 Minute', '15 Minutes', '30 Minutes', '1 Hour', '3 Hours']]]

    @rumps.clicked("Start")
    def start_app(self, _):

        start_button = self.menu["Start"]
        start_button.set_callback(None)

        stop_button = self.menu["Stop"]
        stop_button.set_callback(self.stop_app)

        # print("Starting..")
        self.cw = ChangeWallpaper(self.order)
        self.cw.start()
        rumps.notification("Status", "Process Started",
                           "Wallpaper rotation has Started")

        # rumps.alert("It has started")

    @rumps.clicked("Shuffle")
    def do_shuffle(self, sender):
        sender.state = not sender.state
        self.order = 0

    @rumps.clicked("Time")
    def define_time(self, sender):
        sender.state = not sender.state

    def stop_app(self, _):

        stop_button = self.menu["Stop"]
        stop_button.set_callback(None)

        start_button = self.menu["Start"]
        start_button.set_callback(self.start_app)

        self.cw.kill = True
        # print("Checking if it worked:")
        # time.sleep(2)
        # print("Thread is: " + str(self.cw.isAlive()))
        rumps.notification("Status", "Process stopped",
                           "Wallpaper rotation has stopped")

    @rumps.clicked("About")
    def about_app(self, _):
        rumps.alert(title="About", message='Wallpaper Changer Alpha 0.0.1')
        # rumps.alert("Wallpaper Changer Alpha 0.0.1")


if __name__ == "__main__":
    AwesomeStatusBarApp().run()
