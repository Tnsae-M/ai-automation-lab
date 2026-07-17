from model import Resume
from config import openai_key
from openai import OpenAI

client = OpenAI(api_key=openai_key)

SYSTEM_PROMPT = """You are a resume analyzer. Extract relevant information from resumes and return it in a structured format. The output should be a JSON object with the following fields. 
here is an example of the expected input and output format:
input:
{
SARAH MITCHELL
Automation Expert | RPA & AI Workflow Engineer
Email: sarah.mitchell@example.com | Phone: +1 (555) 234-8890
Location: Austin, TX

PROFESSIONAL SUMMARY
Results-driven automation expert with 7+ years of experience designing and implementing intelligent workflow automation solutions. Skilled in Python, RPA platforms, APIs, and AI-powered integrations. Proven track record of reducing manual workload by up to 80% and improving operational efficiency.

CORE SKILLS
- Python, JavaScript, SQL
- UiPath, Power Automate, Zapier, n8n
- REST APIs, webhooks, OAuth
- AI/LLM integrations, prompt engineering
- Cloud automation, CI/CD, Docker
- Data processing, reporting, ETL

PROFESSIONAL EXPERIENCE
Senior Automation Engineer
TechFlow Solutions | Mar 2022 - Present
- Built AI-powered document processing workflows that reduced invoice handling time by 75%.
- Led automation initiatives across finance, HR, and support teams.
- Integrated OpenAI and Claude APIs into internal tools for lead qualification and triage.

Automation Developer (RPA)
Meridian Business Systems | Jun 2019 - Feb 2022
- Developed over 20 bots for accounts payable, reconciliation, and reporting tasks.
- Built web scraping and API integrations to streamline operational data collection.
- Trained business users on Power Automate and automation best practices.

EDUCATION
B.S. in Computer Science
University of Texas at Austin | 2013 - 2017

CERTIFICATIONS
- UiPath Advanced RPA Developer
- Microsoft Power Automate RPA Developer Associate
- AWS Certified Cloud Practitioner
}

output:
{
   "resume_score": 9,
    "name": "Sarah Mitchell",
    target_job": "Automation Expert | RPA & AI Workflow Engineer",
    "languages": ["Python", "JavaScript", "SQL"],
    "strength": ["Designing and implementing intelligent workflow automation solutions", "Integrating AI-powered tools into business processes", "Reducing manual workload and improving operational efficiency"],
    "weakness": ["Limited experience with certain RPA platforms", "May require additional training for specific enterprise systems"],
    "suggestion": ["Gain experience with additional RPA platforms", "Explore advanced AI/ML techniques for automation", "Participate in cross-functional projects to broaden skill set"]
}
"""
def analyze_resume(resume_text: str) -> Resume:
    response = client.responses.parse(
        model="gpt-5.4-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": resume_text}
        ],
        text_format=Resume

    )
    return response.output_parsed