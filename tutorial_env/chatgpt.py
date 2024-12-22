import os

import openai

from speak import speak


def ai(query):
    key = "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"
    openai.api_key = key
    text = f"OpenAI response for Prompt: {query} \n *************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("openai"):
        os.mkdir("openai")

    with open(f"Openai/{''.join(query.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
    speak("done")


chatstr = ''


def chat(query):
    global chatstr
    print("chatting....")
    openai.api_key = openai.api_key = "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"
    chatstr += f"User: {query}\n Edwin: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speak(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
