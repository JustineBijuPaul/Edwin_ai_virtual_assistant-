import google.generativeai as genai
import os
from speak import speak
import api




def ai(query):
    text = f"Gemini response for Prompt: {query} \n *************************\n\n"
    genai.configure(api_key=api.API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    for chunk in response:
        text += chunk.text
    if not os.path.exists("Gemini"):
        os.mkdir("Gemini")
    with open(f"Gemini/{''.join(query.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
    speak("done")




def chat(query):
    global chatstr
    model = genai.GenerativeModel('gemini-pro')
    print("chatting....")
    genai.configure(api_key=api.API_KEY)
    response = model.generate_content(query)
    for chunk in response:
        res = donot(chunk.text)
        print(res)
        speak(res)


def donot(a):
    special_chars = "*#',\""
    for char in special_chars:
        a = a.replace(char, " ")
    return a

