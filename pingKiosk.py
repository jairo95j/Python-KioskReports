# import os
# import datetime
#
# # Variables
# # Strings
# kioskAppend = "cmp-k-"
# currentDateTime = datetime.datetime.now().strftime("%m-%d-%y-%H-%M" + "\n")
#
# # List
# kioskUp = []
# kioskDown = []
#
#
# def ping_kiosk():
#     # Loop - Ping Kiosk from 1-9
#     for x in range(1, 31):
#         if x < 10:
#             kiosk = (kioskAppend + "0" + str(x))
#             response = os.system("ping -c 1 " + kiosk)
#             # Check for the response...
#             if response == 0:
#                 kioskUp.append(kiosk)
#             else:
#                 kioskDown.append(kiosk)
#         else:
#             kiosk = (kioskAppend + str(x))
#             response = os.system("ping -c 1 " + kiosk)
#             # Check for the response...
#             if response == 0:
#                 kioskUp.append(kiosk)
#             else:
#                 kioskDown.append(kiosk)
#
#
# def kiosk_up(kiosk):
#     kioskUp.append(kiosk)
#     return
#
#
# def kiosk_down(kiosk):
#     kioskDown.append(kiosk)
#     return
#
#
# ping_kiosk()
