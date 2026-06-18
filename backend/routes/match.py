from fastapi import APIRouter
from pydantic import BaseModel
from services.matcher import calculate_match

router = APIRouter()

class MatchRequest(BaseModel):
    resume_skills: list[str]
    jd_skills: list[str]

@router.post("/")
def match(req: MatchRequest):

    return calculate_match(
        req.resume_skills,
        req.jd_skills
    )
