import datetime
from gemini import ai, chat
from sites import site
from speak import speak, takecommand, wish_me
from spotify import ytmu
from vscode import opencode
from whapp import whatsapp
from yt import yt


def rerun():
    while True:
        query = takecommand().lower()
        query = query.replace("edwin", "")
        if 'site' in query:
            site(query)
            rerun()

        if 'play music' in query:
            ytmu()
            rerun()

        elif 'play song' in query:
            ytmu()
            rerun()

        elif 'using artificial intelligence' in query:
            ai(query)
            rerun()

        elif 'youtube' in query:
            yt()
            rerun()

        elif 'open code' in query:
            opencode()
            rerun()

        elif 'whatsapp message' in query:
            whatsapp()
            rerun()

        elif "time" in query:
            this_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{this_time}")
            rerun()

        elif 'exit' in query:
            speak("have a good day mate, see you later")
            exit()

        elif 'stop' in query:
            speak("have a good day mate, see you later")
            exit()

        else:
            chat(query)


if __name__ == '__main__':
    wish_me()
    rerun()
