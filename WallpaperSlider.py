import rumps
import time
from threading import Thread
from ChangeWallpaper import ChangeWallpaper


class AwesomeStatusBarApp(rumps.App):

    rumps.debug_mode(True)

    cw = None

    t1 = None

    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__(
            "Wallpaper Change", "", "trayicon.png")

        self.menu = [
            ('Start'),
            ('Stop'),
            ('Next'),
            ('Resume'),
            None,
            ('Time', ('10 Seconds', '30 Seconds', '1 Minute',
                      '15 Minutes', '30 Minutes', '1 Hour', '3 Hours')),
            ('Shuffle'),
            None,
            ('About')
        ]
        self.order = 1
        self.cw = ChangeWallpaper(self.order)

    @rumps.clicked("Start")
    def start_app(self, _):

        self.cw.start()

        start_button = self.menu["Start"]
        start_button.set_callback(None)

        stop_button = self.menu["Stop"]
        stop_button.set_callback(self.stop_app)

        rumps.notification("Status", "Process Started",
                           "Wallpaper rotation has Started")

    @rumps.clicked("Next")
    def next_wallpaper(self, _):
        self.cw.go_to_next_wallpaper()

    @rumps.clicked("Shuffle")
    def do_shuffle(self, sender):
        sender.state = not sender.state
        if self.order == 1:
            self.order = 0
            self.cw.set_n_order(0)
        else:
            self.order = 1
            self.cw.set_n_order(1)

    @rumps.clicked("Resume")
    def resume_app(self, _):
        self.cw.resume()
        self.cw.kill = False

        stop_button = self.menu["Stop"]
        stop_button.set_callback(self.stop_app)

        start_button = self.menu["Resume"]
        start_button.set_callback(None)

    def stop_app(self, _):

        self.cw.kill = True
        self.cw.pause()

        stop_button = self.menu["Stop"]
        stop_button.set_callback(None)

        start_button = self.menu["Resume"]
        start_button.set_callback(self.resume_app)

        rumps.notification("Status", "Process stopped",
                           "Wallpaper rotation has stopped")

    @rumps.clicked("About")
    def about_app(self, _):
        rumps.alert(title="About", message='Wallpaper Slider Alpha 0.0.1')

    # Time Limits  (Functions)

    @rumps.clicked('Time', '10 Seconds')
    def time_span_10_seconds(self, sender):
        title = sender.title
        sender.state = not sender.state
        self.deselect_all_options(title)
        self.cw.set_time(self.convert_string_to_time(title))

    @rumps.clicked('Time', '30 Seconds')
    def time_span_30_seconds(self, sender):
        title = sender.title
        sender.state = not sender.state
        self.deselect_all_options(title)
        self.cw.set_time(self.convert_string_to_time(title))

    @rumps.clicked('Time', '1 Minute')
    def time_span_1_minute(self, sender):
        title = sender.title
        sender.state = not sender.state
        self.deselect_all_options(title)
        self.cw.set_time(self.convert_string_to_time(title))

    @rumps.clicked('Time', '15 Minutes')
    def time_span_15_minutes(self, sender):
        title = sender.title
        sender.state = not sender.state
        self.deselect_all_options(title)
        self.cw.set_time(self.convert_string_to_time(title))

    @rumps.clicked('Time', '30 Minutes')
    def time_span_30_minutes(self, sender):
        title = sender.title
        sender.state = not sender.state
        self.deselect_all_options(title)
        self.cw.set_time(self.convert_string_to_time(title))

    @rumps.clicked('Time', '1 Hour')
    def time_span_1_hour(self, sender):
        title = sender.title
        sender.state = not sender.state
        self.deselect_all_options(title)
        self.cw.set_time(self.convert_string_to_time(title))

    @rumps.clicked('Time', '3 Hours')
    def time_span_3_hours(self, sender):
        title = sender.title
        sender.state = not sender.state
        self.deselect_all_options(title)
        self.cw.set_time(self.convert_string_to_time(title))

    # Other functions

    def convert_string_to_time(self, string_time):
        splitted = string_time.split(" ", 1)
        number = 0

        if splitted[1] == "Seconds":
            number = int(splitted[0])*1
        elif splitted[1] == "Minutes" or splitted[1] == "Minute":
            number = int(splitted[0])*60
        elif splitted[1] == "Hours" or splitted[1] == "Hour":
            number = int(splitted[0])*3600
        else:
            number = int(splitted[0])*1

        return number

    def deselect_all_options(self, sender):
        for i in self.menu['Time']:
            rest = self.menu['Time'][str(i)]
            if str(i) != str(sender):
                if rest.state:
                    rest.state = not rest.state


if __name__ == "__main__":
    AwesomeStatusBarApp().run()
