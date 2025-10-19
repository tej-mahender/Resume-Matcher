import json
import re

def extract_jd_with_gemini(jd_text, client, model="gemini-2.5-flash"):
    prompt = f"""
Extract the following from the Job Description:
- Required Education
- Required Years of Experience
- Must-have Skills
- Optional Skills

Output strictly as JSON with keys:
education, years_experience, must_have_skills, optional_skills

Job Description:
{jd_text}
"""
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    raw_text = response.text.strip()
    # Remove backticks
    cleaned_text = re.sub(r"^```json\s*|\s*```$", "", raw_text, flags=re.DOTALL)
    cleaned_text = re.sub(r"^```\s*|\s*```$", "", cleaned_text, flags=re.DOTALL)

    try:
        jd_json = json.loads(cleaned_text)
    except json.JSONDecodeError:
        jd_json = {"raw_output": cleaned_text}
    return jd_json
