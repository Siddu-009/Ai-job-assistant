from fastapi import FastAPI

from routes.resume import router as resume_router
from routes.job import router as job_router
from routes.match import router as match_router
from routes.generate import router as generate_router
from cors import setup_cors

app = FastAPI(
    title="AI Job Assistant",
    version="1.0.0"
)

# Resume APIs
app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)

# Job Description APIs
app.include_router(
    job_router,
    prefix="/job",
    tags=["Job"]
)

# Match Score APIs
app.include_router(
    match_router,
    prefix="/match",
    tags=["Match"]
)

# Generate APIs
app.include_router(
    generate_router,
    prefix="/generate",
    tags=["AI Resume"]
)

# Cors
app = FastAPI(
    title="AI Job Assistant",
    version="1.0.0"
)

setup_cors(app)

@app.get("/")
def root():
    return {
        "message": "AI Job Assistant API Running",
        "status": "success"
    }

