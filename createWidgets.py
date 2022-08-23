# import tkinter as tk
# import pingKiosk
#
# kioskDown = pingKiosk.kioskDown
# kioskUp = pingKiosk.kioskUp
#
#
# class createWidgets(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#
#         self.downLabel = tk.Label(self, text="These Kiosk are down:", fg="white", bg="black")
#         self.downLabel.pack()
#
#         for x in range(len(kioskDown)):
#             self.x = tk.Label(self, text=kioskDown[x], fg="black", bg="white")
#             self.x.pack()
#
#         self.upLabel = tk.Label(self, text="These Kiosk are up:", fg="white", bg="black")
#         self.upLabel.pack()
#
#         for x in range(len(kioskUp)):
#             self.x = tk.Label(self, text=kioskUp[x], fg="black", bg="white")
#             self.x.pack()
#
#         self.close_button = tk.Button(self, text="close", fg="black", bg="white",
#                                       command=self.master.destroy)
#         self.close_button.pack()
#
#
# root = tk.Tk()
# app = createWidgets(master=root)
# app.master.title("Kiosk Report")
# app.mainloop()
