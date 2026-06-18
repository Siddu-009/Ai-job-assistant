from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class JobRequest(BaseModel):
    description: str

KNOWN_SKILLS = [
    "AWS",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Linux",
    "Git",
    "GitHub",
    "GitHub Actions",
    "Jenkins",
    "Ansible",
    "Python",
    "Prometheus",
    "Grafana",
    "ArgoCD",
    "Helm"
]

@router.post("/analyze")
def analyze_job(job: JobRequest):

    found = []

    for skill in KNOWN_SKILLS:
        if skill.lower() in job.description.lower():
            found.append(skill)

    return {
        "skills": found
    }
