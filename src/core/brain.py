import os
import google.generativeai as genai
from dotenv import load_dotenv
from core.listen import listen
from core.speak import speak

load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

generation_model = genai.GenerativeModel('gemini-1.5-flash')

def corpinit():
    speak("ShadowCorp is now online. How can I assist you today?")
    chat = generation_model.start_chat(history=[])
    while True:
        user_input = listen()
        if user_input == "":
            continue
        elif user_input is None:
            speak("I didn't catch that. Could you please repeat?")
            continue
        elif "sair" in user_input.lower() or "exit" in user_input.lower():
            speak("Goodbye!")
            break 
        try:
            print("ShadowCorp: Pensando...")
            # Envia a mensagem usando o chat contínuo
            response = chat.send_message(user_input)
            speak(f"ShadowCorp says: {response.text}")
        except Exception as e:
            print(f"Erro: {e}")
            speak("Desculpe, ocorreu um erro ao processar sua resposta.")
if __name__ == "__main__":
    corpinit()