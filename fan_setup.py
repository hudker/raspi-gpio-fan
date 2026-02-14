#!/usr/bin/env python3
import curses
import re

CONFIG_PATH = "/boot/firmware/config.txt"
FAN_REGEX = re.compile(r"^\s*dtoverlay=gpio-fan.*$", re.MULTILINE)

def update_overlay(pin, temp):
    new_line = f"dtoverlay=gpio-fan,gpiopin={pin},temp={temp}"

    with open(CONFIG_PATH, "r") as f:
        content = f.read()

    if FAN_REGEX.search(content):
        # Replace existing line
        content = FAN_REGEX.sub(new_line, content)
    else:
        # Add new line at the end
        content = content.rstrip() + "\n" + new_line + "\n"

    with open(CONFIG_PATH, "w") as f:
        f.write(content)

def main(stdscr):
    curses.curs_set(1)
    stdscr.clear()

    stdscr.addstr(1, 2, "GPIO Fan Setup (Replace-or-Insert Mode)")
    stdscr.addstr(3, 2, "Enter GPIO pin: ")
    stdscr.refresh()
    pin = stdscr.getstr(3, 20, 4).decode()

    stdscr.addstr(5, 2, "Enter temperature (C): ")
    stdscr.refresh()
    temp_c = stdscr.getstr(5, 28, 6).decode()

    temp = int(float(temp_c) * 1000)

    update_overlay(pin, temp)

    stdscr.addstr(8, 2, "Fan overlay updated safely.")
    stdscr.addstr(10, 2, "Reboot required.")
    stdscr.addstr(12, 2, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
