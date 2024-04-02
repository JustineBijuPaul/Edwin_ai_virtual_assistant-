import os

from speak import speak


def opencode():
    codepath = ("C:\\Users\\JUSTINE BIJU PAUL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual "
                "Studio Code\\Visual Studio Code.lnk")
    speak("opening v s code")
    os.startfile(codepath)
    exit()
