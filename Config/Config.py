import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.open_ai_api_key = os.getenv("OPENAI_API_KEY")
        self.punctuition = [".", "?", "!"]
        self.llm = os.getenv("LLM", "gpt-3.5-turbo")
        self.name = os.getenv("NAME", "Alexa")
        self.tempature = float(os.getenv("TEMPATURE", "0.9"))
        self.debug_mode = os.getenv("DEBUG_MODE", "False") == "True"
        self.speak_mode = os.getenv("SPEAK_MODE", "False") == "True"
        self.role = "an ai assistant to help in a smart home"
        self.ws = os.getenv("WS", "True") == "True"