from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_prd(
        product_name,
        problem_statement,
        target_users,
        features
):
    
    prompt = f"""
You are a Senior Product Manager.

Generate a professional PRD.

Product Name:
{product_name}

Problem Statement:
{problem_statement}

Target Users:
{target_users}

Key Features:
{features}

Include:

1. Executive Summary
2. Problem Statement
3. User Personas
4. User Stories
5. Functional Requirements
6. MVP Scope
7. Success Metrics
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content