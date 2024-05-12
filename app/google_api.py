# from config import APY_KEY
import google.generativeai as genai
from constants import *

class GoogleApi:
    def __init__(self) -> None:
        pass

    def chat_response(self, prompt):
        genai.configure(api_key=get_api_key())

        # Set up the model
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
        }

        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        ]

        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)

        convo = model.start_chat(history=[])

        convo.send_message(prompt)
        # print(convo.last.text)
        return convo.last.text

    def max_line_prompt(self, prompt):
        limit_chars = 2000
        if len(prompt) <= limit_chars:
            return prompt
        else:
            return prompt[:limit_chars]

