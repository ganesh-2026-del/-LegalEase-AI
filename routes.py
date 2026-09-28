from fastapi import APIRouter
from pydantic import BaseModel
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.get("/test")
def test():
    return {"message": "Backend working"}

@router.post("/generate")
def generate_doc(data: PromptRequest):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(data.prompt)
        return {"result": response.text}
    except Exception as e:
        return {"error": str(e)}