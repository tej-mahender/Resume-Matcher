import os
import tempfile
import logging
import json
from flask_cors import CORS
from flask import Flask, request, jsonify

from utils.resume_parser import extract_resume_text
from utils.jd_parser import extract_jd_with_gemini
from utils.evaluator import evaluate_resume_with_gemini
from google import genai

from dotenv import load_dotenv
load_dotenv()  # load .env file

# Flask app
app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))


# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)


# Folder to temporarily store uploaded resumes
UPLOAD_FOLDER = "temp_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return "Resume Matcher API is running. Use POST /evaluate_resume to evaluate resumes."


@app.route("/evaluate_resume", methods=["POST"])
def evaluate_resume():
    # Get uploaded file
    file = request.files.get("resume_file")
    jd_text = request.form.get("jd_text")

    if not file or not jd_text:
        return jsonify({
            "status": "error",
            "data": None,
            "error": "Resume file and JD text are required"
        }), 400

    # Save uploaded file temporarily
    temp_path = None
    try:
        # Save uploaded resume to a temporary file
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            file.save(tmp.name)
            temp_path = tmp.name
        logging.info(f"Saved temporary resume file at {temp_path}")

        # Extract resume text
        resume_text = extract_resume_text(temp_path)
        logging.info(f"Extracted resume text ({len(resume_text)} characters)")

        # Process JD (optional Gemini extraction for structured data)
        jd_structured = extract_jd_with_gemini(jd_text, client)

        # Evaluate resume against JD
        report = evaluate_resume_with_gemini(resume_text, jd_structured, client)


        return jsonify({
            "status": "success",
            "data": report,
            "error": None
        })

    except Exception as e:
        logging.error(f"Error during resume evaluation: {e}", exc_info=True)
        return jsonify({
            "status": "error",
            "data": None,
            "error": str(e)
        }), 500

    finally:
        # Clean up temporary file
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
            logging.info(f"Deleted temporary file {temp_path}")


# Global error handler
@app.errorhandler(Exception)
def handle_global_exception(e):
    logging.error(f"Unhandled Exception: {e}", exc_info=True)
    return jsonify({
        "status": "error",
        "data": None,
        "error": "Internal server error. Check logs for details."
    }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)