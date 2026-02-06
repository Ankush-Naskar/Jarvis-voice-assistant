from openai import OpenAI
from data_handling import DataHandling

class ArtificialIntelligence():
    def __init__(self):
        
        data = DataHandling()
        API_KEY=data.get_settings("artificial_intelligence", "open_ai_api_key")
        self.MODEl = data.get_settings("artificial_intelligence", "open_ai_model")
        self.MAX_TOKEN = data.get_settings("artificial_intelligence", "max_token")
        self.ASSISTANT_NAME = data.get_settings("basic", "assistant_name")

        self.client = OpenAI(
                base_url="https://api.groq.com/openai/v1",
                api_key=API_KEY
                )
        
        self.history = [{"role": "system", "content": f"You are {self.ASSISTANT_NAME}, a helpful and friendly AI assistant. Made by Ankush"}]

    def AI(self, prompt):
        self.history.append({"role": "user", "content": prompt}) # Load history
        try:
            completion = self.client.chat.completions.create(
                model=self.MODEl,
                messages=self.history,
                temperature=0.7,
                max_tokens=self.MAX_TOKEN
            )
            response = completion.choices[0].message.content.strip()
            self.history.append({"role": "assistant", "content": response}) # Load History
            return response
        
        except Exception as e:
            return "Sorry, I couldn't process that right now."
            
