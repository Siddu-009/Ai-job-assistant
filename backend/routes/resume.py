from fastapi import APIRouter, UploadFile, File
from services.parser import extract_text_from_pdf
from services.skills import extract_skills
import os

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_DIR, file.filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(filepath)

    skills = extract_skills(text)

    return {
        "filename": file.filename,
        "skills": skills
    }
