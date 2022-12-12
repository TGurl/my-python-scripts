#!/usr/bin/env python

import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # things will go here

        self.set_default_size(600, 250)
        self.set_title("MyApp")

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.swich_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.button = Gtk.Button(label="Hello")
        self.button.connect('clicked', self.hello)
        self.check = Gtk.CheckButton(label="And goodbye?")
        self.switch = Gtk.Switch()
        self.switch.set_active(True)
        self.switch.connect("state-set", self.switch_switched)
        self.label = Gtk.Label(label="A switch")

        self.swich_box.append(self.switch)
        self.swich_box.append(self.label)
        self.swich_box.set_spacing(5)

        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)
        self.box2.append(self.button)
        self.box2.append(self.check)
        self.box2.append(self.swich_box)

    def switch_switched(self, switch, state):
        print(f"The switch has been switched {'on' if state else 'off'}")

    def hello(self, button):
        print("Hello World!")
        print("Trans Rights Are Human Rights!")
        if self.check.get_active():
            print("Goodbye Cruel World!")
            self.close()


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
