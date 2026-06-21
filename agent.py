from groq import Groq
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

api_key = None

try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def generate_prd(product_description):

    prompt = f"""
You are a Principal Product Manager.

Analyze the following product idea:

{product_description}

If users, features or business goals are not provided,
infer them intelligently.

Generate a professional PRD containing:

# Executive Summary

# Product Vision

# Problem Statement

# Target Users

# User Personas

# User Stories

# Functional Requirements

# Non Functional Requirements

# MVP Scope

# Success Metrics

# Risks and Assumptions

# Future Roadmap

Format in markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def competitor_analysis(product_description):

    prompt = f"""
You are a Senior Product Strategist.

Analyze the following product idea:

{product_description}

Generate a competitor research report.

Include:

# Product Summary

# Direct Competitors

For each competitor provide:

- Company
- Product
- Key Features
- Strengths
- Weaknesses

# Indirect Competitors

# Feature Comparison Table

# Market Gaps

# Differentiation Opportunities

# Strategic Recommendations

Format in markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content