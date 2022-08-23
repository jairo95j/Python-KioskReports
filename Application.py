#!/usr/bin/env python3

import tkinter as tk
import os
import datetime

# Variables
# Strings
kioskAppend = "cmp-k-"
currentDateTime = datetime.datetime.now().strftime("%m-%d-%y-%H-%M" + "\n")

# Lists
kioskUp = []
kioskDown = []


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.downLabel = tk.Label(self, text="These Kiosk are down:", fg="white", bg="black")
        self.downLabel.pack()

        for x in range(len(kioskDown)):
            self.x = tk.Label(self, text=kioskDown[x], fg="black", bg="white")
            self.x.pack()

        self.upLabel = tk.Label(self, text="These Kiosk are up:", fg="white", bg="black")
        self.upLabel.pack()

        for x in range(len(kioskUp)):
            self.x = tk.Label(self, text=kioskUp[x], fg="black", bg="white")
            self.x.pack()

        self.close_button = tk.Button(self, text="close", fg="black", bg="white",
                                      command=self.master.destroy)
        self.close_button.pack()

def ping_kiosk():
    # Loop - Ping Kiosk from 1-9
    for x in range(1, 31):
        if x < 10:
            kiosk = (kioskAppend + "0" + str(x))
            response = os.system("ping -c 1 " + kiosk)
            # Check for the response...
            if response == 0:
                kioskUp.append(kiosk)
            else:
                kioskDown.append(kiosk)
        else:
            kiosk = (kioskAppend + str(x))
            response = os.system("ping -c 1 " + kiosk)
            # Check for the response...
            if response == 0:
                kioskUp.append(kiosk)
            else:
                kioskDown.append(kiosk)


def kiosk_up(kiosk):
    kioskUp.append(kiosk)
    return


def kiosk_down(kiosk):
    kioskDown.append(kiosk)
    return


ping_kiosk()
root = tk.Tk()
app = Application(master=root)
app.master.title("Kiosk Report")

app.mainloop()

