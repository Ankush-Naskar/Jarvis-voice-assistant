from openai import OpenAI
from modules.data_handler.data_handling import DataCollecting

class ArtificialIntelligence():
    def __init__(self):
        # Data Loading
        data = DataCollecting()
        API_KEY=data.get_settings("artificial_intelligence", "open_ai_api_key") # API Key
        self.MODEl = data.get_settings("artificial_intelligence", "open_ai_model") # Model Name
        self.MAX_TOKEN = data.get_settings("artificial_intelligence", "max_token") # Max token
        self.ASSISTANT_NAME = data.get_settings("basic", "assistant_name") # Assistant Name

        self.client = OpenAI(
                base_url="https://api.groq.com/openai/v1", # GROQ link
                api_key=API_KEY # API Key
                )
        
        # History saving
        self.history = [{"role": "system", "content": f"You are {self.ASSISTANT_NAME}, a helpful and friendly AI assistant. Made by Ankush"}]

    def AI(self, prompt):
        self.history.append({"role": "user", "content": prompt}) # Load history
        try:
            completion = self.client.chat.completions.create(
                model=self.MODEl, # MODEL NAME
                messages=self.history,
                temperature=0.7,
                max_tokens=self.MAX_TOKEN
            )
            response = completion.choices[0].message.content.strip()
            self.history.append({"role": "assistant", "content": response}) # Load History
            return response
        
        except Exception as e:
            return "Sorry, I couldn't process that right now."
            
