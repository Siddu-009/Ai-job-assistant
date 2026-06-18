from fastapi import APIRouter
from pydantic import BaseModel

from services.ai_resume import generate_resume

router = APIRouter()

class GenerateRequest(BaseModel):
    resume: str
    job_description: str

@router.post("/")
def generate(req: GenerateRequest):

    result = generate_resume(
        req.resume,
        req.job_description
    )

    return {
        "generated_resume": result
    }

