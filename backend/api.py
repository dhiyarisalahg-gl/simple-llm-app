from fastapi import APIRouter, HTTPException
from .models import JournalEntry, AIResponse
from langchain.llms import OpenAI
from .config import get_settings

router = APIRouter()

settings = get_settings()
openai_model = OpenAI(api_key=settings['openai_api_key'])

@router.post("/journal", response_model=AIResponse)
async def process_journal(entry: JournalEntry):
    prompt_quote = f"On {entry.date}, feeling '{entry.mood}' and described as '{entry.description}', generate a motivational quote."
    prompt_song = f"On {entry.date}, feeling '{entry.mood}' and described as '{entry.description}', recommend a song."

    quote_response = openai_model.generate(prompts=[prompt_quote], max_tokens=60)
    song_response = openai_model.generate(prompts=[prompt_song], max_tokens=60)
    
    quote_text = quote_response.generations[0][0].text.strip() if quote_response.generations else "No quote generated"
    song_text = song_response.generations[0][0].text.strip() if song_response.generations else "No song recommendation"

    return AIResponse(quote=quote_text, song_recommendation=song_text)
