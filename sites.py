import webbrowser as wb

from speak import speak

web = [["open AI", "https://www.openai.com"], ["facebook", "https://www.facebook.com"],
       ["blogger", "https://www.blogger.com"], ["linkedin", "https://www.linkedin.com"],
       ["apple", "https://www.apple.com"], ["wordpress", "https://www.wordpress.org"],
       ["microsoft", "https://www.microsoft.com"], ["mozilla", "https://www.mozilla.or"],
       ["cloudflare", "https://www.cloudflare.com"], ["adobe", "https://www.adobe.com"],
       ["europa", "https://www.europa.eu"], ["amazon", "https://www.amazon.com"],
       ["github", "https://www.github.com"], ["samsung", "https://www.samsung.com"],
       ["google", "https://www.google.com"], ["wikipedia", "https://www.wikipedia.com"]]


def site(query):
    for sites in web:
        if f"open {sites[0]}" in query:
            speak(f"opening {sites[0]}")
            wb.open(sites[1])
            break
