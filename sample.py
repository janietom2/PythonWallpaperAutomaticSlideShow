
import rumps
import time

# turn on command line logging information for development - default is off
rumps.debug_mode(True)


@rumps.clicked("About")
def about(sender):
    # can adjust titles of menu items dynamically
    sender.title = 'NOM' if sender.title == 'About' else 'About'
    rumps.alert("This is a cool app!")


# very simple to access nested menu items
@rumps.clicked("Arbitrary", "Depth", "It's pretty easy")
def does_something(sender):
    my_data = {'poop': 88}
    rumps.notification(title='Hi', subtitle='There.',
                       message='Friend!', sound=does_something.sound, data=my_data)


does_something.sound = True


@rumps.clicked("Preferences")
def not_actually_prefs(sender):
    if not sender.icon:
        sender.icon = 'level_4.png'
    sender.state = not sender.state
    does_something.sound = not does_something.sound


# create a new thread that calls the decorated function every 4 seconds
@rumps.timer(4)
def write_unix_time(sender):
    with app.open('times', 'a') as f:  # this opens files in your app's Application Support folder
        f.write('The unix time now: {}\n'.format(time.time()))


@rumps.clicked("Arbitrary")
def change_statusbar_title(sender):
    app.title = 'Hello World' if app.title != 'Hello World' else 'World, Hello'


@rumps.notifications
def notifications(notification):  # function that reacts to incoming notification dicts
    print(notification)


# functions don't have to be decorated to serve as callbacks for buttons
def onebitcallback(sender):
    # this function is specified as a callback when creating a MenuItem below
    print(4848484)


if __name__ == "__main__":
    app = rumps.App("My Toolbar App", title='World, Hello')
    app.menu = [
        # can specify an icon to be placed near text
        rumps.MenuItem('About', dimensions=(18, 18)),
        'Preferences',
        None,  # None functions as a separator in your menu
        {'Arbitrary':
            {"Depth": ["Menus", "It's pretty easy"],
             "And doesn't": ["Even look like Objective C", rumps.MenuItem("One bit", callback=onebitcallback)]}},
        None
    ]
    app.run()
