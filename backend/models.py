from pydantic import BaseModel
from datetime import date

class JournalEntry(BaseModel):
    date: date
    mood: str
    description: str

class AIResponse(BaseModel):
    quote: str
    song_recommendation: str
