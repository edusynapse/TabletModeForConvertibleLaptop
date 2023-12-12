#!/usr/bin/python3

# This code is an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html
# https://gist.github.com/candidtim/7290a1ad6e465d680b68

import os
import signal
import json
import subprocess

import gi
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify



APPINDICATOR_ID = 'tabletmodeindicator'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('/home/surajitray/TabletButton/tablet.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_tbmode = gtk.MenuItem('TabletMode')
    item_tbmode.connect('activate', tbmode)
    menu.append(item_tbmode)


    item_lpmode = gtk.MenuItem('LaptopMode')
    item_lpmode.connect('activate', lpmode)
    menu.append(item_lpmode)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    return menu

def tbmode(_):
    subprocess.call("/home/surajitray/TabletButton/keyboardtouchpaddisable.sh", shell=True)
    return tbmode

def lpmode(_):
    subprocess.call("/home/surajitray/TabletButton/keyboardtouchpadenable.sh", shell=True)
    return lpmode

def quit1(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
