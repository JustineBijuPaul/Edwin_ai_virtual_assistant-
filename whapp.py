<<<<<<< HEAD
import pywhatkit as pwt

from speak import speak
from speak import takecommand


def whatsapp():
    speak("For Whom should i send message")
    contacts = {"name": 1234567890,
                "name": 1234567890,
                }
    to = takecommand()
    speak("what message should i send")
    msg = takecommand()
    speak(f"sending message to {to}")
    try:
        pwt.sendwhatmsg_instantly(f"+91{contacts[to]}", msg)
    except Exception as e:
        speak("error sending message")
        print(e)
        exit()
=======
import pywhatkit as pwt

from speak import speak
from speak import takecommand


def whatsapp():
    speak("For Whom should i send message")
    contacts = {"name": 1234567890,
                "name": 1234567890,
                }
    to = takecommand()
    speak("what message should i send")
    msg = takecommand()
    speak(f"sending message to {to}")
    try:
        pwt.sendwhatmsg_instantly(f"+91{contacts[to]}", msg)
    except Exception as e:
        speak("error sending message")
        print(e)
        exit()
>>>>>>> 14da02a (updated)
