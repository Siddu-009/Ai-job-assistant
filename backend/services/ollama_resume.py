import requests

OLLAMA_URL = "http://ollama:11434/api/generate"

def generate_resume(master_resume, job_description):

    prompt = f"""
You are an ATS Resume Expert.

Master Resume:
{master_resume}

Job Description:
{job_description}

Generate an ATS optimized resume tailored to the job description.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]
