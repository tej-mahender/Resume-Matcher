import json
from google import genai

def evaluate_resume_with_gemini(resume_text, jd_text, client, model="gemini-2.5-flash"):
    prompt = f"""
You are a recruitment assistant. Compare the candidate's resume with the job description.

Resume:
{resume_text}

Job Description:
{jd_text}

Tasks:
1. Give an overall match score (0-100%).
2. Give section-wise match scores (education, experience, skills, projects, certifications, responsibilities).
3. List missing skills or experience per section.
4. Provide actionable suggestions to improve the resume for this job.

Output strictly as valid JSON with these keys:
overall_score, section_scores, missing_items, suggestions
Return only JSON, without any extra formatting, markdown, or code fences.
"""

    # Call the Gemini model
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    raw_text = response.text.strip()

    # Attempt to parse JSON safely
    try:
        resume_eval = json.loads(raw_text)
    except json.JSONDecodeError:
        # If parsing fails, return structured error with raw output
        resume_eval = {
            "error": "Failed to parse JSON from model response",
            "raw_output": raw_text
        }

    return resume_eval
