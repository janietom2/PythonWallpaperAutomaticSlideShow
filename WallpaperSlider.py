import rumps
import time
from ChangeWallpaper import ChangeWallpaper


class AwesomeStatusBarApp(rumps.App):

    # rumps.debug_mode(True)

    cw = None
    order = 1

    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__(
            "Wallpaper Change", "", "trayicon.png")

        self.menu = [
            ('Start'),
            ('Stop'),
            None,
            ('Time', ('10 Seconds', '30 Seconds', '1 Minute',
                      '15 Minutes', '30 Minutes', '1 Hour', '3 Hours')),
            ('Shuffle'),
            None,
            ('About')
        ]

        self.cw = ChangeWallpaper(self.order)

    @rumps.clicked("Start")
    def start_app(self, _):

        start_button = self.menu["Start"]
        start_button.set_callback(None)

        stop_button = self.menu["Stop"]
        stop_button.set_callback(self.stop_app)

        # print("Starting..")
        self.cw.start()
        rumps.notification("Status", "Process Started",
                           "Wallpaper rotation has Started")

        # rumps.alert("It has started")

    @rumps.clicked("Shuffle")
    def do_shuffle(self, sender):
        sender.state = not sender.state
        self.order = 0

    def stop_app(self, _):
        stop_button = self.menu["Stop"]
        stop_button.set_callback(None)

        start_button = self.menu["Start"]
        start_button.set_callback(self.start_app)

        self.cw.kill = True
        print(self.cw.time)

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
