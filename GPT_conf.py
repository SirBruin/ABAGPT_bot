import openai as ai
from random import randint

class GPT:
    def __init__(self, text):
        self.API = ai.api_key = "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"
        self.TEXT = text

    def gpt_response(self):
        system_role = ['and best python programmer', 'and best technology engineer', 'You are a ChatGPT Bot',
                       'you are best senior programmer', 'your a best teacher',
                       'you are best trader and market Analyzer']
        response = ai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    'role': 'system',
                    'content': f'You are a helpful {system_role[randint(0,5)]} '
                               f', upbeat and funny and very best  assistant.'
                },
                {
                    'role': 'user',
                    'content': self.TEXT
                }
                ]
        )
        output_text = response.choices[0]['message']['content']
        return output_text
