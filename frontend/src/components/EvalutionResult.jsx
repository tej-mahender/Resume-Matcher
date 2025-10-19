import React from "react";

export default function EvaluationResult({ report }) {
  if (!report) return null; // prevents errors when report is missing

  const overall = report.overall_score ?? 0;
  const sectionScores = report.section_scores ?? {};
  const missingItems = report.missing_items ?? {};
  const suggestions = report.suggestions ?? [];

  return (
    <div className="mt-6 bg-white p-5 rounded-xl shadow space-y-4">
      <h2 className="text-xl font-semibold">Evaluation Report</h2>

      <div>
        <span className="font-medium">Overall Score: </span>
        {overall}%
      </div>

      <div>
        <h3 className="font-medium">Section Scores:</h3>
        {Object.keys(sectionScores).length > 0 ? (
          <ul className="list-disc pl-5">
            {Object.entries(sectionScores).map(([k, v]) => (
              <li key={k}>
                {k}: {v}%
              </li>
            ))}
          </ul>
        ) : (
          <div>No section scores available.</div>
        )}
      </div>

      <div>
        <h3 className="font-medium">Missing Items:</h3>
        {Object.keys(missingItems).length > 0 ? (
          Object.entries(missingItems).map(
            ([section, items]) =>
              items.length > 0 && (
                <div key={section} className="mt-1">
                  <span className="font-medium">{section}: </span>
                  {items.join(", ")}
                </div>
              )
          )
        ) : (
          <div>None</div>
        )}
      </div>

      <div>
        <h3 className="font-medium">Suggestions:</h3>
        {suggestions.length > 0 ? (
          <ol className="list-decimal pl-5">
            {suggestions.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ol>
        ) : (
          <div>No suggestions.</div>
        )}
      </div>
    </div>
  );
}
