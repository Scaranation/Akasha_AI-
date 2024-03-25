import os
import google.generativeai as genai
from dotenv import load_dotenv

def configure():
    load_dotenv()
    API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=API_KEY)

def start_chat(model_name='gemini-pro'):
    model = genai.GenerativeModel(model_name)
    return model.start_chat(history=[])

def main():
    configure()
    chat = start_chat()

    while True:
        print('Welcome To Akasha')
        question = input("Travelers: ").strip()
        
        if not question:
            break

        response = chat.send_message(question)
        print('\n')
        print(f"AKASHA BOT:  {response.text}")
        print('\n')

if __name__ == "__main__":
    main()
