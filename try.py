import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyA--6yizmNriQHXfjZJMhw26Jeh-gGXie8")

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('who is the president of india')

print(response.text)