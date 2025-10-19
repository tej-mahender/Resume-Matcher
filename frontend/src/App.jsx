import React, { useState } from "react";
import UploadResume from "./components/UploadResume";
import EvaluationReport from "./components/EvalutionResult";
import axios from "axios";
import Loader from "./components/Loader";

export default function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jdText, setJdText] = useState("");
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

//const backendUrl = import.meta.env.VITE_BACKEND_URL;
const backendUrl = "http://127.0.0.1:5000";

const handleEvaluate = async () => {
  setError(null);
  if (!resumeFile) return setError("Please upload a resume file.");
  if (!jdText || jdText.trim().length < 10)
    return setError("Please enter a job description.");

  setLoading(true);
  setReport(null);

  try {
    const formData = new FormData();
    formData.append("resume_file", resumeFile);
    formData.append("jd_text", jdText);

    const response = await axios.post(
      `${backendUrl}/evaluate_resume`,
      formData,
      { headers: { "Content-Type": "multipart/form-data" }, timeout: 120000 }
    );

    if (response.data.status === "success") {
      setReport(response.data.data);
    } else {
      setError(response.data.error || "Unexpected API response.");
    }
  } catch (err) {
    setError(err.message || "Failed to contact backend.");
  } finally {
    setLoading(false);
  }
};


  const resetAll = () => {
    setResumeFile(null);
    setJDText("");
    setReport(null);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-slate-50 p-6 flex justify-center">
      <div className="max-w-4xl w-full space-y-6">
        <h1 className="text-2xl font-bold">Resume Matcher</h1>

        <UploadResume file={resumeFile} setFile={setResumeFile} />

        <div>
          <label className="block text-sm font-medium text-slate-700">
            Job Description
          </label>
          <textarea
            value={jdText}
            onChange={(e) => setJdText(e.target.value)}
            rows={10}
            className="mt-2 w-full rounded-lg border p-2 text-sm"
            placeholder="Paste the job description here..."
          />
        </div>

        {error && (
          <div className="text-red-600 text-sm bg-red-50 p-2 rounded">{error}</div>
        )}

        <div className="flex gap-3">
          <button
            onClick={handleEvaluate}
            className="px-4 py-2 bg-slate-800 text-white rounded-lg"
            disabled={loading}
          >
            {loading ? "Evaluating..." : "Evaluate"}
          </button>
          <button
            onClick={resetAll}
            className="px-4 py-2 border rounded-lg text-slate-700"
          >
            Reset
          </button>
        </div>

        {loading && <Loader />}

        {report && <EvaluationReport report={report} />}
      </div>
    </div>
  );
}
