from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.llms import OpenAI  
import os

load_dotenv()

class JournalEntry(BaseModel):
    mood: str
    description: str

class AIResponse(BaseModel):
    quote: str
    song_recommendation: str

app = FastAPI()

openai_model = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/journal", response_model=AIResponse)
async def process_journal(entry: JournalEntry):
    prompt_quote = f"Based on the mood '{entry.mood}' and the description '{entry.description}', generate a motivational quote."
    prompt_song = f"Based on the mood '{entry.mood}' and the description '{entry.description}', recommend a song."

    quote_response = openai_model.generate(prompts=[prompt_quote], max_tokens=60)
    song_response = openai_model.generate(prompts=[prompt_song], max_tokens=60)
    
    quote_text = quote_response.generations[0][0].text.strip() if quote_response.generations else "No quote generated"
    song_text = song_response.generations[0][0].text.strip() if song_response.generations else "No song recommendation"

    return AIResponse(quote=quote_text, song_recommendation=song_text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
