from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_resume(master_resume, job_description):

    prompt = f"""
    You are an ATS Resume Expert.

    Master Resume:
    {master_resume}

    Job Description:
    {job_description}

    Create an ATS optimized resume.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content
